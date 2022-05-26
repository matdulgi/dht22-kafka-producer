#!/bin/bash

set -x

home=$(cd $(dirname $0) && pwd)
#echo home : $home
if [ ! -d $home/logs ]; then
#  echo log directory
  mkdir $home/logs
fi

#echo $home

logfile=$home/logs/error-kafka-producer.log
if [ ! -f $logfile ]; then
  touch $logfile
fi
 
python3 $home/dht22-kafka-producer.py >> $logfile 2>&1 &

set +x
