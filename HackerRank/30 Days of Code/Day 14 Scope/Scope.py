# Project name : HackerRank: Day 14: Scope
# Link         : https://www.hackerrank.com/challenges/30-scope/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-03
# Description  :
# Status       : Accepted (167017112)
# Tags         : python
# Comment      : 

class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        self.maximumDifference = max(a) - min(a)

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)