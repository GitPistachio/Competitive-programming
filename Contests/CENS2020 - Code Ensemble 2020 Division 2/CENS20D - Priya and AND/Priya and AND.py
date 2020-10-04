# Project name : CodeChef: CENS20D - Priya and AND
# Link         : https://www.codechef.com/CENS2020/problems/CENS20D
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-08-19
# Description  :
# Status       : Accepted (36973514)
# Tags         : python
# Comment      : 

from sys import stdin, stdout


no_of_test_cases = int(stdin.readline())
for _ in range(no_of_test_cases):
    n = int(stdin.readline())
    A = list(map(int, stdin.readline().split()))
    
    no_of_pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            if A[i] == A[i] & A[j]:
                no_of_pairs += 1
    
    stdout.write("{}\n".format(no_of_pairs))