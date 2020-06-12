# Project name : CodeChef: EOEO - The Tom and Jerry Game!
# Link         : https://www.codechef.com/JUNE20B/problems/EOEO
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-06-05
# Description  :
# Status       : Accepted (33719502)
# Tags         : python, game theory
# Comment      : 100

from sys import stdin, stdout


def solve(ts):
    while ts & 1 == 0:
        ts >>= 1
    
    return ts//2


no_of_test_cases = int(stdin.readline())
for _ in range(no_of_test_cases):
    ts = int(stdin.readline())
    no_of_possible_js = solve(ts)
    stdout.write(str(no_of_possible_js) + "\n")
