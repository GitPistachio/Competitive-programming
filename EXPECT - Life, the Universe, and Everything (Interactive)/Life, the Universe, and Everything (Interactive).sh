#!/bin/bash

# Project name : SPOJ: EXPECT - Life, the Universe, and Everything (Interactive)
# Author       : Wojciech Raszka
# Date created : 2019-03-11
# Description  :
# Status       : Accepted (23386996)
# Comment      :

while true
do
  read line
  if [ $line -eq 42 ]
  then
    echo $line
    exit 0
  fi
  echo $line
done
