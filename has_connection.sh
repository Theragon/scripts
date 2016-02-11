#!/usr/bin/env bash
result=$(ip neigh show)
echo $result
if [[ $result == *"REACHABLE"* ]]
then
	echo "connection!";
	exit 0;
else
	echo "no connection";
	exit 1;
fi
