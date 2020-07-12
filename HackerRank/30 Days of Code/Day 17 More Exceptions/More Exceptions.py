# Project name : HackerRank: Day 17: More Exceptions
# Link         : https://www.hackerrank.com/challenges/30-more-exceptions/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-10
# Description  :
# Status       : Accepted (168232857)
# Tags         : python
# Comment      : 

#!/bin/python3

class Calculator:
    @staticmethod
    def power(n, p):
        if n < 0 or p < 0:
            raise Exception('n and p should be non-negative')
        
        return n**p

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
