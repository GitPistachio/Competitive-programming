#!/bin/bash

# Project name : SPOJ: NEWTANK - Tanks
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created :
# Description  :
# Status       : Accepted (23639305)
# Tags         : bash
# Comment      :

read T

for((i = 1; i <= $T; i++))
do
	read v t
	echo "Case #$i: $(($v*$t))"
done
