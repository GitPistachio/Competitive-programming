#!/bin/bash

# Project name : SPOJ: DAYOUT2F - More Dragons
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-05
# Description  :
# Status       : Accepted (23884607)
# Tags         : bash
# Comment      : Only pure vowels

vowels=(a e i o u A E I O U)

read T
for ((t = 1; t <= $T; t++)); do
  read line_of_soldiers
  read start end

  echo -n "Case $t: "
  no_of_dragons=0
  n=$((${#vowels[@]} - 1))
  for i in $(seq 0 $n); do

    let "no_of_dragons+=$(echo ${line_of_soldiers:$start-1:$end-$start+1} | grep -o ${vowels[i]} | wc -l)"
  done
  echo "$no_of_dragons"
done
