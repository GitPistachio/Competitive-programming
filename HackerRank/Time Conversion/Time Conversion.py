# Project name : HackerRank: Time Conversion
# Link         : https://www.hackerrank.com/challenges/time-conversion/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-23
# Description  :
# Status       : Accepted (165433031)
# Tags         : python, time conversion
# Comment      : 

#!/bin/python3

import os
import sys
import time


def timeConversion(s):
    v = time.strptime(s.rstrip(), '%I:%M:%S%p')
    return time.strftime('%H:%M:%S', v)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
