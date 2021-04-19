# Project name : HackerRank: Find Angle MBC
# Link         : https://www.hackerrank.com/challenges/find-angle/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-04-16
# Description  :
# Status       : Accepted (209089726)
# Tags         : python, math, geometry, right triangle, Thales's theorem, trigonometry
# Comment      : 

from math import atan, pi

AB = float(input())
BC = float(input())

print('{}\u00B0'.format(round(atan(AB/BC)*180/pi)))
