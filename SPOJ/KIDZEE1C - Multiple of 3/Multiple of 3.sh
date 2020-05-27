#!/bin/bash

# Project name : SPOJ: KIDZEE1C - Multiple of 3
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-01
# Description  :
# Status       : Accepted (23860998)
# Tags         : bash
# Comment      :

read T
for ((t = 1; t <= $T; t++))
do
	read n
	if [ $n != "" ]; then
		if [ $(($n % 3)) -eq 0 ]; then
			echo $n is a multiple of 3
		else
			echo $n is not a multiple of 3
		fi
	else
		t=$(($t - 1))
	fi
done
