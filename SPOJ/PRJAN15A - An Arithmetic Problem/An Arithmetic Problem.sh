#!/bin/bash

# Project name : SPOJ: PRJAN15A - An Arithmetic Problem
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-06
# Description  :
# Status       : Accepted (23888670)
# Tags         : bash, arithmetic progression
# Comment      :

read T
for ((t = 1; t <= $T; t++)); do
  read a b c n

  if [ $(($c - $b - $b + $a)) -eq 0 ]; then
    echo "Case $t: "
  else
    echo "Case $t: Error"
  fi
done
