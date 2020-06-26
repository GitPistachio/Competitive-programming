# Project name : HackerRank: The Tom and Jerry Game!
# Link         : https://www.hackerrank.com/challenges/simple-array-sum/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-18
# Description  :
# Status       : Accepted (164609180)
# Tags         : python
# Comment      : 

#!/bin/python3

import os
import sys


def simpleArraySum(ar):
    return sum(ar)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
