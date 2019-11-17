#!/bin/bash

# Project name : SPOJ: MOZSAHTF - Sharmeen And Her Two Friends
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-11-12
# Description  :
# Status       : Accepted (24842960)
# Tags         : bash
# Comment      :

read d

if [ $(($d % 2)) -eq 1 ]; then
	echo "Samira"
else
	echo "Rabeya"
fi
