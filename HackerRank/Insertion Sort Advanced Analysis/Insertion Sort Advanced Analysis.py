# Project name : HackerRank: Insertion Sort Advanced Analysis
# Link         : https://www.hackerrank.com/challenges/insertion-sort/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-04-17
# Description  :
# Status       : Accepted (209528424)
# Tags         : python, sorting, inversions count, merege sort
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort function below.
def merge(A, p, q, r):
    i = p
    k = 0
    j = q
    inv_cnt = 0
    T = [None for _ in range(r - p + 1)]
    
    while i <= q - 1 and j <= r:
        if A[i] <= A[j]:
            T[k] = A[i]
            i += 1
        else:
            T[k] = A[j]
            j += 1
            inv_cnt += q - i
        k += 1
    
    if i <= q - 1:
        while i <= q - 1:
            T[k] = A[i]
            i += 1
            k += 1
    else:
        while j <= r:
            T[k] = A[j]
            j += 1
            k += 1
    
    A[p:r + 1] = T
    
    return inv_cnt

def mergeSort(A, p, r):
    inv_cnt = 0
    
    if p < r:
        q = (p + r)//2
        inv_cnt += mergeSort(A, p, q)
        inv_cnt += mergeSort(A, q + 1, r)
        inv_cnt += merge(A, p, q + 1, r)
    
    return inv_cnt

def insertionSort(arr):
    return mergeSort(arr, 0, len(arr) - 1)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
