#!/bin/bash

# Project name : SPOJ: KIDZEE1D - Great Grading Scheme
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-01
# Description  :
# Status       : Accepted (23861992)
# Tags         : bash
# Comment      :

read T
for ((t = 1; t <= $T; t++))
do
	read mark
	if [ $mark -ge 0 ] && [ $mark -le 44 ]; then
		echo Case $t: F
	elif [ $mark -ge 45 ] && [ $mark -le 49 ]; then
		echo Case $t: D
	elif [ $mark -ge 50 ] && [ $mark -le 54 ]; then
		echo Case $t: C
	elif [ $mark -ge 55 ] && [ $mark -le 59 ]; then
		echo Case $t: B-
	elif [ $mark -ge 60 ] && [ $mark -le 64 ]; then
		echo Case $t: B
	elif [ $mark -ge 65 ] && [ $mark -le 69 ]; then
		echo Case $t: B+
	elif [ $mark -ge 70 ] && [ $mark -le 74 ]; then
		echo Case $t: A-
	elif [ $mark -ge 75 ] && [ $mark -le 79 ]; then
		echo Case $t: A
	elif [ $mark -ge 80 ] && [ $mark -le 100 ]; then
		echo Case $t: A+
	else
		echo 1
	fi
done
