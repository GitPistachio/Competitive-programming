# Project name : HackerRank: String Formatting
# Link         : https://www.hackerrank.com/challenges/python-string-formatting/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-16
# Description  :
# Status       : Accepted (169233941)
# Tags         : python
# Comment      : 

n, m = map(int, input().split())

for i in range(n//2):
    print(('.|.'*(2*i + 1)).center(m, '-'))

print('WELCOME'.center(m, '-'))

for i in range(n//2 - 1, -1, -1):
    print(('.|.'*(2*i + 1)).center(m, '-'))
