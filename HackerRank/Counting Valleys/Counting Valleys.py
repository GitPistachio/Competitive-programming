# Project name : HackerRank: Counting Valleys
# Link         : https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-28
# Description  :
# Status       : Accepted (166123320)
# Tags         : python, sliding window technique
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    level = 0
    no_of_valleys = 0
    for step in s:
        if step == 'U':
            level += 1
        else:
            level -= 1
        
        if level == 0:
            if step == 'U':
                no_of_valleys += 1
        
    return no_of_valleys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
