# Project name : CodeChef: CENS20G - Help Martha
# Link         : https://www.codechef.com/CENS2020/problems/CENS20G
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-08-19
# Description  :
# Status       : Accepted (36983490)
# Tags         : python
# Comment      : 

from sys import stdin, stdout
from collections import Counter


no_of_test_cases = int(stdin.readline())
for _ in range(no_of_test_cases):
    operations = stdin.readline().rstrip()
    operations_freq = Counter(operations)
    
    x1, y1 = map(int, stdin.readline().split())
    no_of_queries = int(stdin.readline())
    for _ in range(no_of_queries):
        is_possible = True
        x2, y2 = map(int, stdin.readline().split())
        x = x2 - x1
        y = y2 - y1
        if ((x < 0 and operations_freq['L'] < -x) or
            (x > 0 and operations_freq['R'] < x) or
            (y < 0 and operations_freq['D'] < -y) or
            (y > 0 and operations_freq['U'] < y)):
            is_possible = False
        
        if is_possible:
            stdout.write('YES {}\n'.format(abs(x) + abs(y)))
        else:
            stdout.write('NO\n')
