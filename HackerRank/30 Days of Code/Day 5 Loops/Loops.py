# Project name : HackerRank: Day 5: Loops
# Link         : https://www.hackerrank.com/challenges/30-loops/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-23
# Description  :
# Status       : Accepted (165429904)
# Tags         : python
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    for i in range(1, 11):
        print('{} x {} = {}'.format(n, i, n*i))