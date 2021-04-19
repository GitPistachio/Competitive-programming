# Project name : HackerRank: Triangle Quest 2
# Link         : https://www.hackerrank.com/challenges/triangle-quest-2/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-04-17
# Description  :
# Status       : Accepted (209195163)
# Tags         : python, math, integer sequence A002275 (OEIS)
# Comment      : 

for i in range(1,int(input())+1):
    print(((10**i - 1)//9)**2)
