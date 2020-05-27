#!/bin/bash

# Project name : SPOJ: KIDZEE1O - Kings on an Infinite Chessboard
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-01
# Description  :
# Status       : Accepted (23862847)
# Tags         : bash
# Comment      :

read T
for ((t = 1; t <= $T; t++))
do
	read r1 c1 r2 c2
	r=$(($r1 - r2))
	r=${r#-}

	c=$(($c1 - c2))
	c=${c#-}

	if [ $r -le $c ]; then
		d=$r
	else
		d=$c
	fi

	echo "Case $t: $(($r + $c - $d))"
done
