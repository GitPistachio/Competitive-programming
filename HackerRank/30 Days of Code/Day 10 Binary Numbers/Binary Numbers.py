# Project name : HackerRank: Day 10: Binary Numbers
# Link         : https://www.hackerrank.com/challenges/30-binary-numbers/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-28
# Description  :
# Status       : Accepted (166238536)
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
    max_no_of_ones = 1
    current_no_of_ones = 0
    while n > 0:
        if n & 1 == 1:
            current_no_of_ones += 1
            if current_no_of_ones > max_no_of_ones:
                max_no_of_ones = current_no_of_ones
        else:
            current_no_of_ones = 0
        
        n >>= 1
    
    print(max_no_of_ones)