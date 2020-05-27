#!/bin/bash

# Project name : SPOJ: SMPWOW - Wow
# Author       : Wojciech Raszka
# Date created : 2019-02-24
# Description  :
# Status       : Accepted (23289893)
# Comment      :

read n

Wow="W"

for  ((i=0; i<$n; i++))
do
  Wow="${Wow}o"
done
Wow="${Wow}w"

echo $Wow
