# Project name : HackerRank: Strings: Making Anagrams
# Link         : https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-19
# Description  :
# Status       : Accepted (169702298)
# Tags         : python
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from string import ascii_lowercase

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    freq_a = Counter(a)
    freq_b = Counter(b)

    no_of_corrections = 0
    for c in ascii_lowercase:
        no_of_corrections += abs(freq_a[c] - freq_b[c])
    
    return no_of_corrections


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
