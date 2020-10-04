# Project name : HackerRank: collections.Counter()
# Link         : https://www.hackerrank.com/challenges/collections-counter/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-10-03
# Description  :
# Status       : Accepted (182396975)
# Tags         : python
# Comment      : 

from collections import Counter

no_of_shoes = int(input())

shoes_by_size = Counter(map(int, input().split()))

no_of_customers = int(input())

earned_money = 0
for _ in range(no_of_customers):
    size, price = map(int, input().split())
    if shoes_by_size[size] > 0:
        earned_money += price
        shoes_by_size[size] -= 1

print(earned_money)
