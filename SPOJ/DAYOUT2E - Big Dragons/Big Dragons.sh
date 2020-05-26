#!/bin/bash

# Project name : SPOJ: DAYOUT2E - Big Dragons
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-05
# Description  :
# Status       : Accepted (23884553)
# Tags         : bash
# Comment      :

read T
for ((t = 1; t <= $T; t++)); do
  read line_of_soldiers
  read dragon

  m=${#dragon}
  n=$((${#line_of_soldiers} - $m + 1))
  no_of_dragons=0
  for i in $(seq 1 $n); do
    if [ ${line_of_soldiers:i-1:$m} == $dragon ]; then
      let "no_of_dragons++"
    fi
  done
  echo "Case $t: $no_of_dragons"
done
