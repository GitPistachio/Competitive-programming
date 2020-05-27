#!/bin/bash

# Project name : SPOJ: GOO - Game Of Ones
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-04
# Description  :
# Status       : Accepted (23571513)
# Tags         : bash integer sequence A100498 and A001792 (OEIS)
# Comment      : left part: a(n) = 2^n, right part a(n) = (n + 2)*2^(n - 1)

read T

for ((t = 0; t < $T; t++))
do
  read n
  l=$(echo "2^($n - 1)" | bc)
  r=$(bc <<< "($n + 1)*2^($n - 1)/2")
  echo $l $r
done
