#!/bin/bash

# Project name : SPOJ: KIDZEE1M - Seconds Apart
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-01
# Description  :
# Status       : Accepted (23862576)
# Tags         : bash
# Comment      :

read T
for ((t = 1; t <= $T; t++)); do
	read n
	echo -n "Case $t:"
	no_of_years=$(($n/31104000))
	if [ $no_of_years -gt 1 ]; then
		echo -n " $no_of_years years"
	elif [ $no_of_years -eq 1 ]; then
		echo -n " $no_of_years year"
	fi
	n=$(($n - $no_of_years*31104000))

	no_of_months=$(($n/2592000))
	if [ $no_of_months -gt 1 ]; then
		echo -n " $no_of_months months"
	elif [ $no_of_months -eq 1 ]; then
		echo -n " $no_of_months month"
	fi
	n=$(($n - $no_of_months*2592000))

	no_of_days=$(($n/86400))
	if [ $no_of_days -gt 1 ]; then
		echo -n " $no_of_days days"
	elif [ $no_of_days -eq 1 ]; then
		echo -n " $no_of_days day"
	fi
	n=$(($n - $no_of_days*86400))


	no_of_hours=$(($n/3600))
	if [ $no_of_hours -gt 1 ]; then
		echo -n " $no_of_hours hours"
	elif [ $no_of_hours -eq 1 ]; then
		echo -n " $no_of_hours hour"
	fi
	n=$(($n - $no_of_hours*3600))

	no_of_minutes=$(($n/60))
	if [ $no_of_minutes -gt 1 ]; then
		echo -n " $no_of_minutes minutes"
	elif [ $no_of_minutes -eq 1 ]; then
		echo -n " $no_of_minutes minute"
	fi
	n=$(($n - $no_of_minutes*60))

	if [ $n -gt 1 ]; then
		echo -n " $n seconds"
	elif [ $n -eq 1 ]; then
		echo -n " $n second"
	fi

	echo ""
done
