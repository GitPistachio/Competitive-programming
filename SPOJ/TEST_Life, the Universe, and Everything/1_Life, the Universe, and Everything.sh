#!/bin/bash

# Project name : SPOJ: TEST - Life, the Universe, and Everything
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created :
# Description  :
# Status       : 
# Tags         : bash
# Comment      :

while true
do
  read line
  if [ $line -eq 42 ]
  then
    exit 0
  fi
  echo $line
done
