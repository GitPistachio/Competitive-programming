# Project name : HackerRank: Sock Merchant
# Link         : https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-28
# Description  :
# Status       : Accepted (166122311)
# Tags         : python
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    sock_in_color = [False]*101

    no_of_matching_socks = 0
    for color in ar:
        if sock_in_color[color]:
            no_of_matching_socks += 1
            sock_in_color[color] = False
        else:
            sock_in_color[color] = True
    
    return no_of_matching_socks


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()


    f.write(result + '\n')

    f.close()
