# Project name : HackerRank: Day 29: Bitwise AND
# Link         : https://www.hackerrank.com/challenges/30-bitwise-and/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-16
# Description  :
# Status       : Accepted (169457945)
# Tags         : python
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        if (k - 1) | k <= n:
            print(k - 1)
        else:
            print(k - 2)


