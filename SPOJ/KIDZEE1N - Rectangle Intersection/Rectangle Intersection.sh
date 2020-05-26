#!/bin/bash

# Project name : SPOJ: KIDZEE1N - Rectangle Intersection
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-01
# Description  :
# Status       : Accepted (23862791)
# Tags         : bash, intersection of rectangles
# Comment      :

read T
for ((t = 1; t <= $T; t++))
do
	read x1 y1 x2 y2
	read x3 y3 x4 y4
	if [ $y3 -ge $y2 ] || [ $y1 -ge $y4 ]; then
		echo "Case $t: No"
	elif [ $x3 -ge $x2 ] || [ $x1 -ge $x4 ]; then
		echo "Case $t: No"
	else
		echo "Case $t: Yes"
	fi
done
