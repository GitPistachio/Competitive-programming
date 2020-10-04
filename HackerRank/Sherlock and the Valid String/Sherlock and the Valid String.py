# Project name : HackerRank: Sherlock and the Valid String
# Link         : https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-19
# Description  :
# Status       : Accepted (169712383)
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

# Complete the isValid function below.
def isValid(s):
    freq_s = Counter(s)
    freq_freq = Counter()

    for c in ascii_lowercase:
        if freq_s[c] != 0:
            freq_freq[freq_s[c]] += 1

    if len(freq_freq) > 2:
        return 'NO'
    
    if len(freq_freq) == 1:
        return 'YES'

    if freq_freq[1] == 1:
        return 'YES'
    x, y = freq_freq.items()


    #print(freq_s)
    #print(freq_freq)
    if x[1] > 1 and y[1] > 1:
        return 'NO'

    if abs(x[0] - y[0]) > 1:
        return 'NO'
    
    return 'YES'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
