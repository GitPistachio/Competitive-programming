#!/bin/bash

# Project name : SPOJ: ALICESIE - Alice Sieve
# Author       : Wojciech Raszka
# Date created : 2019-03-16
# Description  :
# Status       : Accepted (23426591)
# Comment      : The first and only (n + 1)/2 numbers are unmarked.

read T

for ((t = 1; t <= T; t++ ))
do
  read n
  echo $((($n + 1)/2))
done
