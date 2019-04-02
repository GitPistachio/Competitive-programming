#!/bin/bash

# Project name : SPOJ: CDRSANJ - CODER FIRST PROBLEM
# Author       : Wojciech Raszka
# Date created : 2019-04-02
# Description  :
# Status       : Accepted (23554223)
# Tags         : bash
# Comment      : F(n) = n for n <= 2 and F(2^k*m) = 2*k where m = 0 or m is odd for the rest n F(n) = 0

read x

if [ $x -lt 3 ]; then
  echo $x
else
  F=0
  while [ $x -gt 0 ] && [ $(($x % 2)) -eq 0 ]
  do
    F=$(($F+2))
    x=$(($x/2))
  done

  echo $F
fi
