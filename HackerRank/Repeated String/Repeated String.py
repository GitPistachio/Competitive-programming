# Project name : HackerRank: Repeated String
# Link         : https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-30
# Description  :
# Status       : Accepted (166471544)
# Tags         : python
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    sample_size = len(s)
    q, r = divmod(n, sample_size)
    count_a = 0
    for c in s:
        if c == 'a':
            count_a += 1
    
    count_a *= q
    
    i = 0
    while i < r:
        if s[i] == 'a':
            count_a += 1
        i += 1
    return count_a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
