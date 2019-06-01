#!/bin/bash

# Project name : SPOJ: KIDZEE1G - Multiples
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-01
# Description  :
# Status       : Accepted (23862088)
# Tags         : bash
# Comment      :

read T
for ((t = 1; t <= $T; t++))
do
	read x n
	echo -n Case $t:
	for ((i = 1; i <= $n; i++))
	do
		if [ $(($i*$x)) -le $n ]; then
			echo -n " $(($i*$x))"
		else
			break
		fi
	done
	echo ""
done
