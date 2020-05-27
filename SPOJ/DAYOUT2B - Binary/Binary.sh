#!/bin/bash

# Project name : SPOJ: DAYOUT2B - Binary
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-05
# Description  :
# Status       : Accepted (23884283)
# Tags         : bash
# Comment      :

read T
for ((t = 0; t < $T; t++)); do
  read d
  n=$((2**(d - 1)))
  n2=$((2*n))
  if [[ $d -eq 1 ]]; then
    echo 0
  fi
  for ((i = $n; i < n2; i++)); do
    echo "obase=2;$i" | bc
  done
done
