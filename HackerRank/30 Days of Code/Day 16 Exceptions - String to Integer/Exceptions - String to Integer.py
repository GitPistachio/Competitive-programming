# Project name : HackerRank: Day 16: Exceptions - String to Integer
# Link         : https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-10
# Description  :
# Status       : Accepted (168231188)
# Tags         : python
# Comment      : 

#!/bin/python3

import sys


S = input().strip()

try:
    val = int(S)
    print(val)
except ValueError:
    print('Bad String')
