# Project name : HackerRank: Frequency Queries
# Link         : https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-18
# Description  :
# Status       : Accepted (169506190)
# Tags         : python
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the freqQuery function below.
def freqQuery(queries):
    a = Counter()
    b = Counter()

    ans = []
    for q, x in queries:
        if q == 1:
            b[a[x]] -= 1
            a[x] += 1
            b[a[x]] += 1
        elif q == 2:
            if a[x] > 0:
                b[a[x]] -= 1
                a[x] -= 1
                b[a[x]] += 1
        elif q == 3:
            if b[x] > 0:
                ans.append(1)
            else:
                ans.append(0)
    
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()

