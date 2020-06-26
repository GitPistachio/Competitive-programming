# Project name : HackerRank: Day 6: Let's Review
# Link         : https://www.hackerrank.com/challenges/30-review-loop/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-25
# Description  :
# Status       : Accepted (165648152)
# Tags         : python
# Comment      : 

no_of_test_cases = int(input())

for _ in range(no_of_test_cases):
    text = input().rstrip()
    n = len(text)
    odd = text[1:n:2]
    even = text[0:n:2]
    print(even, odd)