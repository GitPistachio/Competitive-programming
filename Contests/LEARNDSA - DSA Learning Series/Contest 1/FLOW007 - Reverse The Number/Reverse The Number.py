# Project name : CodeChef: FLOW007 - Reverse The Number
# Link         : https://www.codechef.com/LRNDSA01/problems/FLOW007
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio
# Date created : 2020-05-31
# Description  :
# Status       : Accepted (33527003)
# Tags         : python
# Comment      :

from sys import stdin, stdout

no_of_test_cases = int(stdin.readline())

for _ in range(no_of_test_cases):
    n = int(stdin.readline().strip()[::-1])
    stdout.write("{}\n".format(n))
