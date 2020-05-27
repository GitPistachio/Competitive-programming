#!/bin/bash

# Project name : SPOJ: KIDZEE1H - Digital Triangle
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-01
# Description  :
# Status       : Accepted (23862116)
# Tags         : bash
# Comment      :

read T
for ((t = 1; t <= $T; t++))
do
	read d h

	echo Case $t:
	for ((i = 0; i < $h; i++)); do
		for ((j = 0; j <= $i; j++)); do
			echo -n $d
		done
		echo ""
	done
done
