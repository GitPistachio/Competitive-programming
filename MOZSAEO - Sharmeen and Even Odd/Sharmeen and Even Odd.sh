# Project name : SPOJ: MOZSAEO - Sharmeen and Even Odd
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created :
# Description  :
# Status       : Accepted (23669655)
# Tags         : bash
# Comment      :

#!/bin/bash

read T

for((t = 0; t < $T; t++))
do
	read a b
	a="${a: -1}"
	b="${b: -1}"
	if [ $((($a + $b) % 2)) -eq 1 ]; then
		echo odd
	else
		echo even
	fi
done
