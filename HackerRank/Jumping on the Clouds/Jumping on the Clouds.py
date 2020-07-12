# Project name : HackerRank: Jumping on the Clouds
# Link         : https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-30
# Description  :
# Status       : Accepted (166467677)
# Tags         : python, game theory
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    n = len(c)

    i = 0
    no_of_jumps = 0
    while i < n - 2:
        if c[i + 2] == 0:
            i += 2
        else:
            i += 1
        no_of_jumps += 1
    
    if i != n - 1:
        no_of_jumps += 1
    
    return no_of_jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
