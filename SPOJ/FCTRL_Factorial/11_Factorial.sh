#!/bin/bash

# Project name : SPOJ: FCTRL - Factorial
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created :
# Description  :
# Status       : Accepted (23571513)
# Tags         : bash, math, factorial, noumber of zeros at the end of an number, integer sequence A027868 (OEIS)
# Comment      :

read T
for  ((i=1; i<=$T; i++))
do
  read n
  echo $(($n/5 + $n/25 + $n/125 + $n/625 + $n/3125 + $n/15625 + $n/78125 + $n/390625 + $n/1953125 + $n/9765625 +$n/48828125 + $n/244140625))
done
