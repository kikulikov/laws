# laws

`ls` for AWS EC2 instances to list them in a short table format. Allows to filter nodes by tag or name. Shorthand alternative to `aws ec2 describe-instances --filters "Name=tag:environment,Values=qa" | jq ".Reservations[].Instances[].PrivateIpAddress"`

## Examples

`laws`

`laws qa`

`laws -p myprofile cassandra`

## Installation

```
pip install laws
```

## PyPi link

https://pypi.python.org/pypi/laws

## Useful resources

http://peterdowns.com/posts/first-time-with-pypi.html

```
git tag 0.X -m "Version bumped to 0.X"
git push --tags origin master
python setup.py sdist upload -r pypi
```
