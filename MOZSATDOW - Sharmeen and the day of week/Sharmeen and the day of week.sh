#!/bin/bash

# Project name : SPOJ: MOZSATDOW - Sharmeen and the day of week
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-11-13
# Description  :
# Status       : Accepted (24854405)
# Tags         : bash
# Comment      :

days=(Friday Saturday Sunday Monday Tuesday Wednesday Thursday)

read n

echo ${days[$(($n % 7))]}
