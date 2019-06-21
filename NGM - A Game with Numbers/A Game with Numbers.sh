#!/bin/bash

# Project name : SPOJ: NGM - A Game with Numbers
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-21
# Description  :
# Status       : Accepted (23955554)
# Tags         : bash, game theory
# Comment      :

read n

if [ $(($n % 10)) -eq 0 ]; then
  echo 2
else
  echo 1
  echo $(($n % 10))
fi
