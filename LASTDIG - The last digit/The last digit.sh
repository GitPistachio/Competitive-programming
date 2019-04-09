#!/bin/bash

# Project name : SPOJ: LASTDIG - The last digit
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-01
# Description  :
# Status       : Accepted (23545257)
# Tags         : bash, number theory, last digit
# Comment      :

C=(0 0 0 0 1 1 1 1 2 4 8 6 3 9 7 1 4 6 4 6 5 5 5 5 6 6 6 6 7 9 3 1 8 4 2 6 9 1 9 1)

read T

for ((t = 0; t < T; t++ ))
do
  read a b
  a=$(($a % 10))
  if [ $b -eq 0 ]; then
	   echo 1
  else
  	b=$((($b - 1) % 4))
  	echo ${C[a*4 + b]}
  fi
done
