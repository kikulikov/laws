#!/usr/bin/env python

import argparse
import boto3
import sys
from tabulate import tabulate
from subprocess import Popen, PIPE, call, STDOUT

class TerminalColours:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def xstr(s):
    return '' if s is None else str(s)


def paint(data, colour):
    return [colour + xstr(s) + TerminalColours.ENDC for s in data]

hostNames = ['ubuntu', 'ec2-user']
rawHeaders = ["NO", "ID", "NAME", "PRIVATE IP", "PUBLIC IP", "VPC", "TYPE", "STATE"]
errors = ["Permission denied", "Connection timed out", "Connection refused"]
colouredHeaders = paint(rawHeaders, TerminalColours.HEADER)


def find_name(inst):
    if inst.tags is not None:
        for pair in inst.tags:  # loop tags
            if pair['Key'] == 'Name' and pair['Value'] is not None:
                return pair['Value']
    return ''


def build_row(inst):
    return [inst.id, find_name(inst), inst.private_ip_address,
    inst.public_ip_address, inst.vpc_id, inst.instance_type, inst.state['Name']]


def get_instances(profile, region):
    session = boto3.Session(profile_name=profile)
    ec2_resource = session.resource('ec2', region_name=region)
    return ec2_resource.instances.all()


def parse_args():
    parser = argparse.ArgumentParser(description='Simple AWS EC2 table view')
    parser.add_argument('-p', '--profile', nargs='?', help='aws profile')
    parser.add_argument('-r', '--region', nargs='?', help='Specify Custom Region')
    parser.add_argument('search', nargs='*', help='search string')
    return parser.parse_args()


def filter_instances(instances, searches):
    data = []
    for inst in instances:
        if inst.tags and searches:
            founds = []
            for s in searches:  # loop search strings
                for tag in inst.tags:  # loop instance tags
                    if s in tag['Value']:
                        founds.append(True)
                        break
            if len(founds) == len(searches) and all(founds):
                data.append(build_row(inst))
        elif not searches:
            data.append(build_row(inst))
    return data


def paint_data_row(row):
    if row[7] == 'stopped':
        return paint(row, TerminalColours.FAIL)
    elif row[7] == 'running':
        return paint(row, TerminalColours.OKGREEN)
    return row


def paint_data(data):
    return [paint_data_row(s) for s in data]


def retrieve_data(args):
    data = filter_instances(get_instances(args.profile, args.region), args.search)
    sortedData = sorted(data, key=lambda x: x[1])
    [x.insert(0,i+1) for i, x in enumerate(sortedData)]
    return sortedData

def printer(colouredHeaders, colouredData):
    print(tabulate(colouredData, headers=colouredHeaders, tablefmt="simple"))

def sshWrapper(ip):
    for hostname in hostNames:
        print "Trying hostname as "+str(hostname)
        command = ['ssh -o ConnectTimeout=5 -t -t '+hostname+'@'+str(ip)]
        x = Popen(command, stderr=PIPE, shell=True)
        (output, err) = x.communicate()
        p_status = x.wait()
        if not p_status:
            return False
    return True

def sshInstance(rawData):
    if not rawData:
        return
    try:
        number = int(raw_input("Enter SSH instance to connect: "))
    except (KeyboardInterrupt, SystemExit, EOFError):
        print "\nExiting"
        sys.exit(0)
    privateIP = rawData[number-1][3]
    publicIP = rawData[number-1][4]
    print ("ec2-ssh connecting")
    err = sshWrapper(privateIP)
    if not err or not publicIP:
        print "Exiting"
        return
    print "Trying with Public IP"
    err = sshWrapper(publicIP)
    if err:
        print "Unable to Connect"
        return False
    return True

def main():
    args = parse_args()
    rawData = retrieve_data(args)
    colouredData = paint_data(rawData)
    printer(colouredHeaders, colouredData)
    sshInstance(rawData)


if __name__ == "__main__":
    main()
