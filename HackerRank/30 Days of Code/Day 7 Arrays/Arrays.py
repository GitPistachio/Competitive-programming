# Project name : HackerRank: Day 7: Arrays
# Link         : https://www.hackerrank.com/challenges/30-arrays/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-25
# Description  :
# Status       : Accepted (165778594)
# Tags         : python
# Comment      : 

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    print(' '.join(map(str, arr[::-1])))