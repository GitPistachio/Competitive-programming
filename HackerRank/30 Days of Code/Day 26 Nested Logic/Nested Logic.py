# Project name : HackerRank: Day 26: Nested Logic
# Link         : https://www.hackerrank.com/challenges/30-nested-logic/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-14
# Description  :
# Status       : Accepted (168848109)
# Tags         : python
# Comment      : 

from sys import stdin, stdout
from datetime import date

day, month, year = map(int, stdin.readline().split())


actual_return_date = date(year, month, day)


day, month, year = map(int, stdin.readline().split())
expected_return_date = date(year, month, day)

fine = 0

if actual_return_date > expected_return_date:
    if actual_return_date.year == expected_return_date.year:
        if actual_return_date.month == expected_return_date.month:
            fine = (actual_return_date.day - expected_return_date.day)*15
        else:
            fine = (actual_return_date.month - expected_return_date.month)*500
    else:
        fine = 10000

stdout.write(str(fine))