#!/usr/bin/env bash

function get_ips()
{
	result=$(ifconfig | awk '/inet addr/{print substr($2,6)}')
	ips=($result)
	length=${#ips[@]}
}

while true; do
	get_ips
	if [[ "$length" -lt 2 ]]; then
			echo "no network"
			echo "sleeping for a minute"
			echo "length:" $length
			sleep 30
			echo "trying again"
		else
			break
		fi
done
echo "found network, starting pushbullet-indicator"
/opt/extras.ubuntu.com/pushbullet-indicator/bin/pushbullet-indicator
