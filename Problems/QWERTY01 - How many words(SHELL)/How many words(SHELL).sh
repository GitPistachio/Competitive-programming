#!/bin/bash

# Project name : SPOJ: QWERTY01 - How many words(SHELL)
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-03-24
# Description  :
# Status       : Accepted (23483578)
# Tags         : bash
# Comment      : 200

read word_to_find

no_of_equals=0
read word
while [ "$word" != "end" ]
do
	if [ "$word" = "$word_to_find" ]
	then
		let no_of_equals=no_of_equals+1
	fi
	read word
done

echo $no_of_equals
