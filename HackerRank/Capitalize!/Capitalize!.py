# Project name : HackerRank: Capitalize!
# Link         : https://www.hackerrank.com/challenges/capitalize/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-16
# Description  :
# Status       : Accepted (169244429)
# Tags         : python
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return ' '.join(map(lambda x: x.capitalize(), s.split(' ')))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
