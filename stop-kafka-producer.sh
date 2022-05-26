#!/bin/bash

filename=dht22-kafka-producer.py

home=$(cd $(dirname $0) && pwd)
gpiotmp=bcm283x

# read from pid file

pid=$(ps -ef | grep $filename | grep -v 'grep' | awk '{print $2}' | head -1)

if [ ! -z $pid ]; then
  kill $pid
  dht kafka producer terminated
fi

pid=$(ps -ef | grep $gpiotmp | grep -v 'grep' | awk '{print $2}' | head -1)
if [ ! -z $pid ]; then
  kill $pid
  libgpiod terminated
fi
