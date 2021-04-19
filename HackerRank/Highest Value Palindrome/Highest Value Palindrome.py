# Project name : HackerRank: Highest Value Palindrome
# Link         : https://www.hackerrank.com/challenges/richie-rich/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-04-16
# Description  :
# Status       : Accepted (208985100)
# Tags         : python, palindrome
# Comment      :  

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the highestValuePalindrome function below.
def highestValuePalindrome(s, n, k):
    min_no_of_changes = 0
    for i in range(n//2):
        if s[i] != s[n - i - 1]:
            min_no_of_changes += 1
            
    if min_no_of_changes > k:
        return '-1'
    
    highest_value_palindrome = ''
    for i in range(n//2):
        if k - min_no_of_changes > 1:
            if s[i] != s[n - i - 1]:
                if s[i] != '9' and s[n - i - 1] != '9':
                    highest_value_palindrome += '9'
                    k -= 2
                else:
                    if s[i] > s[n - i - 1]:
                        highest_value_palindrome += s[i]
                    else:
                        highest_value_palindrome += s[n - i - 1]
                    k -= 1
                min_no_of_changes -= 1
            elif s[i] != '9': # s[i] is equal to s[n - i - 1]:
                highest_value_palindrome += '9'
                k -= 2
            else:
                highest_value_palindrome += s[i]
        elif k - min_no_of_changes == 1:
            if s[i] != s[n - i - 1]:
                if s[i] != '9' and s[n - i - 1] != '9':
                    highest_value_palindrome += '9'
                    k -= 2
                else:
                    if s[i] > s[n - i - 1]:
                        highest_value_palindrome += s[i]
                    else:
                        highest_value_palindrome += s[n - i - 1]
                    k -= 1
                min_no_of_changes -= 1
            else:
                highest_value_palindrome += s[i]
        elif s[i] != s[n - i - 1]: # in this case min_no_of_changes must equal to or less than k
            if s[i] > s[n - i - 1]:
                highest_value_palindrome += s[i]
            else:
                highest_value_palindrome += s[n - i - 1]
            k -= 1
            min_no_of_changes -= 1
        else:
            highest_value_palindrome += s[i]

    if n&1:
        if k > 0:
            return highest_value_palindrome + '9' + highest_value_palindrome[::-1]

        return highest_value_palindrome + s[n//2] + highest_value_palindrome[::-1]
    
    return highest_value_palindrome + highest_value_palindrome[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    s = input()

    result = highestValuePalindrome(s, n, k)

    fptr.write(result + '\n')

    fptr.close()
