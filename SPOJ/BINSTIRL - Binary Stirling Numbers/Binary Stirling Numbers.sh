#!/bin/bash

# Project name : SPOJ: BINSTIRL - Binary Stirling Numbers
# Author       : Wojciech Raszka
# Date created : 2019-03-31
# Description  :
# Status       : Accepted (23533595)
# Tags         : bash, the Stirling number of the second kind, the parity of a Stirling number of the second kind, Sierpiński triangle
# Comment      :

read T

for ((t = 0; t < T; t++))
do
  read n m

  if [ $m -eq 0 ] && [ $n -gt 0 ]; then
    echo 0
  else
    z=$(($n - ($m + 2)/2))
    w=$((($m - 1)/2))
    if [ $(($z&$w)) -eq $w ]; then
      echo 1
    else
      echo 0
    fi
  fi
done
