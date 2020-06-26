# Project name : HackerRank: Birthday Cake Candles
# Link         : https://www.hackerrank.com/challenges/birthday-cake-candles/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-22
# Description  :
# Status       : Accepted (165274959)
# Tags         : python, console patters, staircase
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    max_a = 0
    no_of_blew_candles = 0

    for a in ar:
        if a > max_a:
            max_a = a
            no_of_blew_candles = 1
        elif a == max_a:
            no_of_blew_candles += 1
    
    return no_of_blew_candles

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
