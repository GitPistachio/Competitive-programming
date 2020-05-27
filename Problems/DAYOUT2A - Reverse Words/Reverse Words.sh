#!/bin/bash

# Project name : SPOJ: DAYOUT2A - Reverse Words
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-05
# Description  :
# Status       : Accepted (23884097)
# Tags         : bash
# Comment      :

read T
for ((t = 0; t < $T; t++)); do
  read sentence
  words=(${sentence})
  n=${#words[@]}
  echo -n ${words[$(($n - 1))]}
  for ((i = $(($n - 2)); i >= 0; i--)); do
    echo -n " ${words[i]}"
  done
  echo ""
done
