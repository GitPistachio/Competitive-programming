# Project name : HackerRank: Python If-Else
# Link         : https://www.hackerrank.com/challenges/py-if-else/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-15
# Description  :
# Status       : Accepted (169048802)
# Tags         : python
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    if n & 1:
        print('Weird')
    elif n <= 5:
        print('Not Weird')
    elif n <= 20:
        print('Weird')
    else:
        print('Not Weird')

