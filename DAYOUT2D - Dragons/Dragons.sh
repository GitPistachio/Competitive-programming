#!/bin/bash

# Project name : SPOJ: DAYOUT2D - Dragons
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-05
# Description  :
# Status       : Accepted (23884478)
# Tags         : bash
# Comment      :

read T
for ((t = 1; t <= $T; t++)); do
  read line_of_soldiers
  read dragon

  echo -n "Case $t: "
  echo $line_of_soldiers | grep -o $dragon | wc -l
done
