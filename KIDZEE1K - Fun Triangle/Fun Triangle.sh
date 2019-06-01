#!/bin/bash

# Project name : SPOJ: KIDZEE1K - Fun Triangle
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-01
# Description  :
# Status       : Accepted (23862337)
# Tags         : bash
# Comment      :

read T
for ((t = 1; t <= $T; t++))
do
	read a h
	echo "Case $t: $(($a*$h))"
done
