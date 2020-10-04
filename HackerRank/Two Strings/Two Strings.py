# Project name : HackerRank: Two Strings
# Link         : https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-15
# Description  :
# Status       : Accepted (169046833)
# Tags         : python
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys
from string import ascii_lowercase 

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    for c in ascii_lowercase:
        if c in s1 and c in s2:
            return 'YES'
    
    return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s1 = input()

        s2 = input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

