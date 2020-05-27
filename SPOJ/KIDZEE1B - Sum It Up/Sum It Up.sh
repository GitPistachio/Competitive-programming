#!/bin/bash

# Project name : SPOJ: KIDZEE1B - Sum It Up
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-01
# Description  :
# Status       : Accepted (23860945)
# Tags         : bash
# Comment      :

read T
for ((t = 1; t <= $T; t++))
do
	read x y z
	echo Case $t: Sum of $x, $y and $z is $(($x + $y + $z))
done
