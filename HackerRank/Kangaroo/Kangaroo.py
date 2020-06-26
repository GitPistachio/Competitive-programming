# Project name : HackerRank: Kangaroo
# Link         : https://www.hackerrank.com/challenges/kangaroo/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-26
# Description  :
# Status       : Accepted (165923151)
# Tags         : python
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if x1 < x2:
        d = x2 - x1
        v = v1 - v2
    else:
        d = x1 - x2
        v = v2 - v1
    
    if d != 0 and v <=0:
        return 'NO'

    if d % v == 0:
        return 'YES'

    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()
