# Project name : HackerRank: Lily's Homework
# Link         : https://www.hackerrank.com/challenges/lilys-homework/forum
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-04-06
# Description  :
# Status       : Accepted (207621923)
# Tags         : python, sorting, minimum no of swaps to sort array
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the lilysHomework function below.
def lilysHomework(arr):
    return min(minNoOfSwapsAsc(arr), minNoOfSwapsDesc(arr))

def minNoOfSwapsDesc(arr):
    positions = [x[0] for x in sorted(enumerate(arr), key=lambda x: x[1], reverse=True)]
    
    n = len(arr)
    visited = [False for _ in range(n)]
    ans = 0
    for i in range(n):
        if visited[i] or positions[i] == i:
            continue
        
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = positions[j]
            cycle_size += 1
        
        if cycle_size > 0:
            ans += (cycle_size - 1)
    
    return ans

def minNoOfSwapsAsc(arr):
    positions = [x[0] for x in sorted(enumerate(arr), key=lambda x: x[1], reverse=False)]
    
    n = len(arr)
    visited = [False for _ in range(n)]
    ans = 0
    for i in range(n):
        if visited[i] or positions[i] == i:
            continue
        
        cycle_size = 0
        j = i
        while not visited[j]:
            visited[j] = True
            j = positions[j]
            cycle_size += 1
        
        if cycle_size > 0:
            ans += (cycle_size - 1)
    
    return ans
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

