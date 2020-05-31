# Project name : CodeChef: LOSTWKND - Lost Weekends
# Link         : https://www.codechef.com/LTIME84B/problems/LOSTWKND
# Try it on    : https://ideone.com/mtLUBm
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-05-30
# Description  :
# Status       : Accepted(33452042)
# Tags         : python
# Comment      : 100

from sys import stdin, stdout

no_of_test_cases = int(stdin.readline())

for _ in range(no_of_test_cases):
    A1, A2, A3, A4, A5, P = map(int, stdin.readline().split()) 
    if P*(A1 + A2 + A3 + A4 + A5) > 120:
        stdout.write("Yes\n")
    else:
        stdout.write("No\n")
    