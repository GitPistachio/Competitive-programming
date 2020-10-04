# Project name : HackerRank: Array Manipulation
# Link         : https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-17
# Description  :
# Status       : Accepted (169042130)
# Tags         : python, difference array, range update query O(1)
# Comment      : 



#!/bin/python3

import math
import os
import random
import re
import sys

def arrayManipulation(n, queries):
    diff_arr = [0]*n
    
    for left_idx, right_idx, k in queries:
        left_idx -= 1
        right_idx -= 1
        
        diff_arr[left_idx] += k
        
        if right_idx < n - 1:
            diff_arr[right_idx + 1] -= k
    
    max_a = 0
    a = 0
    for d in diff_arr:
        a += d
        if a > max_a:
            max_a = a
    
    return max_a
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
