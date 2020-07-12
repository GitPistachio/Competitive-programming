# Project name : HackerRank: Apple and Orange
# Link         : https://www.hackerrank.com/challenges/apple-and-orange/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-27
# Description  :
# Status       : Accepted (166091443)
# Tags         : python, time conversion
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    no_of_pick_up_apples = 0
    for d in apples:
        x = a + d
        if s <= x and x <= t:
            no_of_pick_up_apples += 1
    
    no_of_pick_up_oranges = 0
    for d in oranges:
        x = b + d
        if s <= x and x <= t:
            no_of_pick_up_oranges += 1
    
    return (no_of_pick_up_apples, no_of_pick_up_oranges)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    result = countApplesAndOranges(s, t, a, b, apples, oranges)
    print(result[0])
    print(result[1])
