# Project name : HackerRank: Merge Sort: Counting Inversions
# Link         : https://www.hackerrank.com/challenges/ctci-merge-sort/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-19
# Description  :
# Status       : Accepted (169682757)
# Tags         : python
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys

def merge(arr, temp_arr, left, mid, right):
    i = left
    k = 0
    j = mid + 1
    inv_cnt = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            i += 1
        else:
            temp_arr[k] = arr[j]
            inv_cnt += mid - i + 1
            j += 1
        k += 1
    
    while i <= mid:
        temp_arr[k] = arr[i]
        i += 1
        k += 1
    
    while j <= right:
        temp_arr[k] = arr[j]
        j += 1
        k += 1
    
    for i in range(right - left + 1):
        arr[left + i] = temp_arr[i]
    
    return inv_cnt

def mergeSortWithInversionCount(arr, temp_arr, left, right):
    if left >= right:
        return 0
    
    if left == right - 1:
        if arr[left] > arr[right]:
            arr[left], arr[right] = arr[right], arr[left]
            return 1
        
        return 0

    inv_cnt = 0

    if left < right:
        mid = (left + right) >> 1

        inv_cnt += mergeSortWithInversionCount(arr, temp_arr, left, mid)
        inv_cnt += mergeSortWithInversionCount(arr, temp_arr, mid + 1, right)
        inv_cnt += merge(arr, temp_arr, left, mid, right)
    
    return inv_cnt

# Complete the countInversions function below.
def countInversions(arr):
    n = len(arr)
    temp_arr = [0]*n
    return mergeSortWithInversionCount(arr, temp_arr, 0, n - 1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()
