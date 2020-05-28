#!/bin/bash

# Project name : SPOJ: HUBULLU - Hubulullu
# Link		   : https://www.spoj.com/problems/HUBULLU/
# Try it on    : https://ideone.com/W3UDAh
# Author       : Wojciech Raszka
# Email        : contact@gitpistachio.site
# Date created : 2019-03-16
# Description  :
# Status       : Accepted (26042419)
# Tags         : bash, game theory
# Comment      :

read T

for ((t = 1; t <= T; t++ ))
do
  read n
  echo $((($n + 1)/2))
done
