#!/usr/bin/env python

import argparse
import boto.ec2
from tabulate import tabulate


def build_row(inst):
    return [inst.id, inst.tags['Name'], inst.ip_address,
            inst.public_dns_name, inst.vpc_id, inst.state]


def build_headers():
    return ["Id", "Name", "Public IP", "Public DNS", "VPC", "State"]


def get_instances():
    conn = boto.ec2.connect_to_region('eu-west-1')
    return conn.get_all_instances()


def parse_args():
    parser = argparse.ArgumentParser(description='Simple AWS EC2 grep')
    # parser.add_argument('--foo', nargs='?', help='foo help')
    parser.add_argument('search', nargs='+', help='search string')
    return parser.parse_args()


def filter_instances(instances, args):
    data = []
    for res in instances:
        for inst in res.instances:
            count = len(data)
            for key, val in inst.tags.iteritems():  # loop tags
                for s in args.search:  # chech search strings
                    if s in val:
                        data.append(build_row(inst))
                        break  # break if found
                if count < len(data):
                    break  # break if found
    return data


def main():
    data = filter_instances(get_instances(), parse_args())
    data = sorted(data, key=lambda x: x[1])
    print tabulate(data, headers=build_headers(), tablefmt="orgtbl")

if __name__ == "__main__":
    main()
