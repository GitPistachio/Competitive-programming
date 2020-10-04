# Project name : HackerRank: Count Triplets
# Link         : https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-18
# Description  :
# Status       : Accepted (169503689)
# Tags         : python
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
    c = Counter(arr)  # possible thirds elements of progression
    a = Counter()  # possilbe first elements of triplets
    no_of_triplets = 0
    for j in arr:  # loop over middle elements of triplets
        i = j//r
        k = j*r
        c[j] -= 1
        if not j % r and c[k] and a[i]:
            no_of_triplets += a[i]*c[k]
        a[j] += 1
    return no_of_triplets

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()

