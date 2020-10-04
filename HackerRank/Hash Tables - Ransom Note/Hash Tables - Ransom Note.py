# Project name : HackerRank: Hash Tables - Ransom Note
# Link         : https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-15
# Description  :
# Status       : Accepted (169044080)
# Tags         : python, frequnecy table
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    alailable_words = Counter(magazine)

    for word in note:
        if alailable_words[word] <= 0:
            return 'No'

        alailable_words[word] -= 1

    return 'Yes'


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
