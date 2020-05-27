#!/bin/bash

# Project name : SPOJ: DAYOUT2G - Find Them All
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-05
# Description  :
# Status       : Accepted (23884768)
# Tags         : bash
# Comment      :

vowels=(a e i o u A E I O U)
m=$((${#vowels[@]} - 1))

read T
for ((t = 1; t <= $T; t++)); do
  read sentence

  echo "Case $t:"
  n=${#sentence}

  consonants=""
  for i in $(seq 1 $n); do
    l=${sentence:i-1:1}
    is_vowel=false
    for j in $(seq 0 $m); do
      if [ ${vowels[j]} == $l ]; then
        echo -n $l
        is_vowel=true
        break
      fi
    done
    if [ $is_vowel = false ] && [ $l != " " ]; then
      consonants=$consonants$l
    fi
  done
  echo ""
  echo $consonants
  echo ""
done
