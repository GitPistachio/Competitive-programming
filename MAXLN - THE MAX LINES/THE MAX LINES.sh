#!/bin/bash

# Project name : SPOJ: MAXLN - THE MAX LINES
# Author       : Wojciech Raszka
# Date created : 2019-03-15
# Description  :
# Status       : Accepted (23420815)
# Comment      : s(x) = 2r^2 -2xr + sqrt(2r^2 + 2xr), thus the max is s(0.125/r - r) = (2r)^2 + 0.25

read T

for ((t = 1; t <= T; t++ ))
do
  read r
  s=$(echo "2*2*$r*$r + 0.25" | bc -l)
  printf "Case $t: %.2f\n" "$s"
done
