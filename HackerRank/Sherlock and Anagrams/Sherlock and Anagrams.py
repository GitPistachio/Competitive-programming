# Project name : HackerRank: Sherlock and Anagrams
# Link         : https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-18
# Description  :
# Status       : Accepted (169491599)
# Tags         : python
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sherlockAndAnagrams function below.
def isAnagram(s1, s2):
    c2 = Counter(s2)
    for c in s1:
        c2[c] -= 1
        if c2[c] < 0:
            return False
    
    return True

def sherlockAndAnagrams(s):
    n = len(s)
    no_of_angs = 0
    for word_len in range(1, n):
        for i in range(n - word_len):
            a = sorted(s[i:i + word_len]) 
            for j in range(i + 1, n - word_len + 1):
                if a == sorted(s[j:j + word_len]):
                    no_of_angs += 1

    return no_of_angs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

