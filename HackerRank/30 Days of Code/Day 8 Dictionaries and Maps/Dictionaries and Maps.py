# Project name : HackerRank: Day 8: Dictionaries and Maps
# Link         : https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-26
# Description  :
# Status       : Accepted (165921169)
# Tags         : python
# Comment      : 

from sys import stdin


no_of_entries = int(input())

phone_book = {}
for _ in range(no_of_entries):
    name, phone_number = input().split()
    phone_book[name] = phone_number


for name in stdin:
    name = name.strip()
    if name not in phone_book:
        print('Not found')
    else:
        print('{}={}'.format(name, phone_book[name]))
