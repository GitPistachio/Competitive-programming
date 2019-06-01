#!/bin/bash

# Project name : SPOJ: KIDZEE1P - Progression
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-01
# Description  :
# Status       : Accepted (23862865)
# Tags         : bash, arithmetic progression, geometric progression
# Comment      :

read T
for ((t = 1; t <= $T; t++))
do
	read a b c

	if [ $(($c - $b - $b + $a)) -eq 0 ]; then
			if [ $(($b*$b - $a*$c)) -eq 0 ]; then
				echo "Case $t: Both"
			else
				echo "Case $t: Arithmetic Progression"
			fi
	elif [ $(($b*$b - $a*$c)) -eq 0 ]; then
		echo "Case $t: Geometric Progression"
	else
		echo "Case $t: None"
	fi
done
