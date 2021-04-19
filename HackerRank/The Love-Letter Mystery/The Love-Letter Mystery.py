# Project name : HackerRank: The Love-Letter Mystery
# Link         : https://www.hackerrank.com/challenges/the-love-letter-mystery/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-04-15
# Description  :
# Status       : Accepted (208979498)
# Tags         : python, palindrome
# Comment      :  

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def theLoveLetterMystery(s):
    # Change word s to palindrome
    n = len(s)
    n = len(s)
    
    ans = 0
    for i in range(n//2):
        ans += abs(ord(s[i]) - ord(s[n - i - 1]))
    
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()


