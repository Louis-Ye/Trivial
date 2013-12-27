#!/bin/bash

subNet=$1
from=$2
to=$3
cur=$from

function is_IP_there {
	ping -c 1 $1 > /dev/null && echo "$1 exists"
}

while [[ $cur -le $to ]] ; do
	IP_addr="$subNet$cur"
	is_IP_there $IP_addr &
	cur=$(($cur+1))
done

