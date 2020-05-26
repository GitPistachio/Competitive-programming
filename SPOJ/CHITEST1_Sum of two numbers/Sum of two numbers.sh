#!/bin/bash

# Project name : SPOJ: Sum of two numbers
# Author       : Wojciech Raszka
# Date created : 2019-02-10
# Description  :
# Status       : Accepted (23205366)
# Comment      :

read i
until [ $i -lt 0 ]
do
  read a b
  echo "$a+$b" | bc
  let i-=1
done
