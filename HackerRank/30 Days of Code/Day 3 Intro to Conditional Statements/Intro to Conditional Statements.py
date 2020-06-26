# Project name : HackerRank: Day 3: Intro to Conditional Statements
# Link         : https://www.hackerrank.com/challenges/30-conditional-statements/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-20
# Description  :
# Status       : Accepted (165021331)
# Tags         : python
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

    if n & 1 == 1:
        print('Weird')
    elif 2 <= n <= 5:
        print('Not Weird')
    elif 6 <= n <= 20:
        print('Weird')
    elif n > 20:
        print('Not Weird')
