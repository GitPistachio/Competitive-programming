# Project name : HackerRank: Collections.namedtuple()
# Link         : ttps://www.hackerrank.com/challenges/py-collections-namedtuple/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-04-17
# Description  :
# Status       : Accepted (209228117)
# Tags         : python
# Comment      : 

from collections import namedtuple

no_of_sudents = int(input())


field_names = input()
Mark = namedtuple('Mark',field_names)

sum_of_marks = 0
for _ in range(no_of_sudents):
    mark = Mark(*(input().split()))
    sum_of_marks += int(mark.MARKS)

print(sum_of_marks/no_of_sudents)
