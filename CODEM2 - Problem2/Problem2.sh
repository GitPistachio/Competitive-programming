#!/bin/bash

# Project name : SPOJ: CODEM2 - Problem2
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-03
# Description  :
# Status       : Accepted (23562683)
# Tags         : bash, Fermat Last Theorem, Diophantine equation, probability theory, pythagorean triple
# Comment      : From given condition is result as a solving equation x^n + y^2 = z^2 for n > 2 which has no solution in integer domain

read T

for ((t = 0; t < $T; t++))
do
  read n x y
  if [ $n -eq 1 ]; then
    echo $(($x + $y))
  elif [ $n -eq 2 ]; then
    echo "sqrt($x*$x + $y*$y)" | bc
  else
    echo impossible
  fi
done
