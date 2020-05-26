#!/bin/bash

# Project name : SPOJ: MANGOES - Real Mangoes for Ranjith
# Author       : Wojciech Raszka
# Date created : 2019-03-17
# Description  :
# Status       : Accepted (23433248)
# Comment      :

read T

for ((t = 1; t <= T; t++ ))
do
  read n
  if (($n % 2 == 0))
  then
    echo $((($n - 2)*($n - 2)/4 % $n))
  else
    echo $((($n - 1)*($n - 1)/4 % $n))
  fi
done
