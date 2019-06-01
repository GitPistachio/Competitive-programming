#!/bin/bash

# Project name : SPOJ: KIDZEE1E - Sort them All
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-01
# Description  :
# Status       : Accepted (23862021)
# Tags         : bash
# Comment      :

read T
for ((t = 1; t <= $T; t++))
do
	read n1 n2 n3
	if [ $n1 -le $n2 ]; then
		if [ $n3 -ge $n2 ]; then
			echo Case $t: $n1 $n2 $n3
		elif [ $n3 -ge $n1 ]; then
			echo Case $t: $n1 $n3 $n2
		else
			echo Case $t: $n3 $n1 $n2
		fi
	else
		if [ $n3 -le $n2 ]; then
			echo Case $t: $n3 $n2 $n1
		elif [ $n3 -le $n1 ]; then
			echo Case $t: $n2 $n3 $n1
		else
			echo Case $t: $n2 $n1 $n3
		fi
	fi
done
