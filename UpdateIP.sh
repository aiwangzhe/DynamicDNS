#!/bin/bash

cd -P $(dirname $0)

[ ! -e '/usr/bin/curl' ] && yum -y install curl
WanIp=`curl ipv4.icanhazip.com`
LastIp=`cat ~/Last_IP.txt`
if [ "$WanIp" != "$LastIp" ]
then
    echo "your public ip has changed!"
    python AliRequest.py --ip=${WanIp}
    code=$?
    echo "update domain request result code: $code"
    if [ "$code" = "0" ]
    then
       echo $WanIp > ~/Last_IP.txt
    fi
else
    echo "you public ip not changed!"
fi

