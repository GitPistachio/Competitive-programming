#!/bin/bash

# Project name : SPOJ: GUANGGUN - 111…1 Squared
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-01
# Description  :
# Status       : Accepted (23571331)
# Tags         : bash integer sequence A080151 (OEIS)
# Comment      : a(n) = floor(n/9)*81 + (n mod 9)^2


while read n; do
  echo $((($n/9)*81 + ($n % 9)*($n % 9)))
done
