# Project name : HackerRank: Write a function
# Link         : https://www.hackerrank.com/challenges/write-a-function/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-15
# Description  :
# Status       : Accepted (169095879)
# Tags         : python
# Comment      : 

def is_leap(year):
    if year % 4:
        return False

    if year % 100 == 0 and year % 400:
        return False
    
    return True

year = int(input())
print(is_leap(year))
