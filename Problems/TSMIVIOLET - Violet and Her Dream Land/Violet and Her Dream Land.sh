#!/bin/bash

# Project name : SPOJ: TSMIVIOLET - Violet and Her Dream Land
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-15
# Description  :
# Status       : Accepted (23635481)
# Tags         : bash
# Comment      :

read day_of_week

if [ $day_of_week == Monday ]; then
	echo Macaroon
elif [ $day_of_week == Tuesday ]; then
	echo Toffee
elif [ $day_of_week == Wednesday ]; then
	echo Waffles
elif [ $day_of_week == Thursday ]; then
	echo Taco
elif [ $day_of_week == Friday ]; then
	echo "French Fries"
elif [ $day_of_week == Saturday ]; then
	echo Sandwich
else
	echo Soup
fi
