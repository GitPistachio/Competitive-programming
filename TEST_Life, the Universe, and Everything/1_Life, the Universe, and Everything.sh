#!/bin/bash
while true
do
  read line
  if [ $line -eq 42 ]
  then
    exit 0
  fi
  echo $line
done
