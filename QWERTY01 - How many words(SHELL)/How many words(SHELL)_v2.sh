#!/bin/bash

# Project name : SPOJ: QWERTY01 - How many words(SHELL)
# Author       : Wojciech Raszka
# Date created : 2019-03-24
# Description  :
# Status       :
# Tags         : bash
# Comment      : 109

read f

n=0
read w
while [ "$w" != "end" ]
do
	if [ "$w" = "$f" ]
	then
		let n=n+1
	fi
	read w
done

echo $n
