#!/bin/bash

# Project name : SPOJ: EBOXES - Empty Boxes
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created :
# Description  :
# Status       : Accepted (23643085)
# Tags         : bash, math
# Comment      : O(1) solution. Answer N + K*(F - N)/(K - 1)

read T

for((t = 0; t < $T; t++))
do
  read N K R F

  echo $(($N + $K*($F - $N)/($K - 1)))
done
