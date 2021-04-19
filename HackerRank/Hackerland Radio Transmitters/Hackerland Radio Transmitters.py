# Project name : HackerRank: Hackerland Radio Transmitters
# Link         : https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-04-18
# Description  :
# Status       : Accepted (209417286)
# Tags         : python
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerlandRadioTransmitters function below.
def hackerlandRadioTransmitters(x, k):
    n = len(x)
    no_of_transmitters = 1
    last_choosed_house = None
    last_house_without_coverage = 0
    x.sort()
    i = 1
    while i < n:
        if x[i] - x[last_house_without_coverage] > k:
            last_choosed_house = i - 1
            no_of_transmitters += 1
            while i < n:
                if x[i] - x[last_choosed_house] > k:
                    last_house_without_coverage = i
                    break
                i += 1
            else:
                no_of_transmitters -= 1
                break
        else:
            i += 1
    
    return no_of_transmitters

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()

