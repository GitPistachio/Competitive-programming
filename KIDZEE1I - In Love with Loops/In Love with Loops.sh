#!/bin/bash

# Project name : SPOJ: KIDZEE1I - In Love with Loops
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-01
# Description  :
# Status       : Accepted (23862159)
# Tags         : bash
# Comment      :

read T
for ((t = 1; t <= $T; t++))
do
	read A B C

	echo Case $t:
	for ((x = 0; x <= $A; x++)); do
		for ((y = $(($x + 1)); y <= $B; y++)); do
			for ((z = $(($y + 1)); z <= $C; z++)); do
				echo $x $y $z
			done
		done
	done
done
