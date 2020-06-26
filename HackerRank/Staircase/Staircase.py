# Project name : HackerRank: Staircase
# Link         : https://www.hackerrank.com/challenges/staircase/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-22
# Description  :
# Status       : Accepted (165255914)
# Tags         : python, console patters, staircase
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        print(' '*(n - i - 1) + '#'*(i + 1))

if __name__ == '__main__':
    n = int(input())

    staircase(n)
