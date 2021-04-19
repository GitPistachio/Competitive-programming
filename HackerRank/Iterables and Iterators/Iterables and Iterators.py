# Project name : HackerRank: Iterables and Iterators
# Link         : https://www.hackerrank.com/challenges/iterables-and-iterators/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-04-18
# Description  :
# Status       : Accepted (209326051)
# Tags         : python, math, probability
# Comment      : 

from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

no_of_combinations = 0
no_of_combinations_without_letter_a = 0
for c in combinations(letters, r=k):
    if 'a' in c:
        no_of_combinations_without_letter_a += 1
    
    no_of_combinations += 1

print(no_of_combinations_without_letter_a/no_of_combinations)
