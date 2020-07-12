# Project name : HackerRank: Day 11: 2D Arrays
# Link         : https://www.hackerrank.com/challenges/30-2d-arrays/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-29
# Description  :
# Status       : Accepted (166392174)
# Tags         : python, hourglass
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys

def hourglass(arr, li, lj):
    return (arr[li][lj] + arr[li][lj + 1] + arr[li][lj + 2] +
                          arr[li + 1][lj + 1] +
            arr[li + 2][lj] + arr[li + 2][lj + 1] + arr[li + 2][lj + 2])

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    n = len(arr)
    m = len(arr[0])
    max_sum_of_hours = -7*9
    for li in range(n - 2):
        for lj in range(m - 2):  # left bottom corner og hourglass
            sum_of_hours = hourglass(arr, li, lj)
            if sum_of_hours > max_sum_of_hours:
                max_sum_of_hours = sum_of_hours
    
    print(max_sum_of_hours)
