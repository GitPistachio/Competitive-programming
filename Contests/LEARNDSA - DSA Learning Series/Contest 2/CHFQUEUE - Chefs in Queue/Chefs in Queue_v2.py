# Project name : CodeChef: CHFQUEUE - Chefs in Queue
# Link         : https://www.codechef.com/LRNDSA02/problems/CHFQUEUE
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-19
# Description  :
# Status       : Time Limit Exceeded (34542710)
# Tags         : python, linear data structure, modular arithmetic, nearest smaller value algorithm
# Comment      :


from sys import exit, stdin, stdout
from collections import deque

MOD = 1000000007

no_of_chiefs, no_of_seniority_levels = map(int, stdin.readline().split())
chiefs = [int(x) for x in stdin.readline().split()]
fearfulness = 1
stack = deque()
i = 0
while i < no_of_chiefs:
    if not stack or chiefs[stack[-1]] <= chiefs[i]:
        stack.append(i)
        i += 1
    else:
        while stack and chiefs[stack[-1]] > chiefs[i]:
            fearfulness = (fearfulness*(i - stack[-1] + 1)) % MOD
            stack.pop()

stdout.write(str(fearfulness) +'\n')
