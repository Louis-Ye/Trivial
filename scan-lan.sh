#!/bin/bash

function is_IP_there {
	ping -c 4 $1 > /dev/null && echo "$1"
}

subNet=$1
from=$2
to=$3
echo "Following IP may exist:"

pidA=()
cur=$from
while [[ $cur -le $to ]] ; do
	IP_addr="$subNet$cur"
	is_IP_there $IP_addr &
	pidA+=($!)
	cur=$(($cur+1))
done

for item in ${pidA[@]} ; do
	wait $item
done

