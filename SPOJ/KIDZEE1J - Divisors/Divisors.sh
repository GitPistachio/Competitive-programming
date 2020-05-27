#!/bin/bash

# Project name : SPOJ: KIDZEE1J - Divisors
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-01
# Description  :
# Status       : Accepted (23862322)
# Tags         : bash
# Comment      :

read T
for ((t = 1; t <= $T; t++))
do
	read n

	echo -n Case $t:
	tail=""
	for ((i = 1; i*i <= $n; i++)); do
		if [ $(($n % $i)) -eq 0 ]; then
			echo -n " $i"
			if [ $(($i*$i)) -ne $n ]; then
				tail=" $(($n/$i))$tail"
			fi
		fi
	done
	echo "$tail"
done
