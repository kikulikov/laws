#!/bin/bash
set -o nounset
set -o errexit
set -o pipefail

aws ec2 describe-instances --color off --output table --query "Reservations[].Instances[].[Tags[?Key==\`type\`]|[0].Value,Tags[?Key==\`Name\`]|[0].Value,PublicIpAddress,PublicDnsName,State.Name]" | grep running | awk -F'|' '{print $2, $3, $4, $5}'
