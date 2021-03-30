# Project name : CodeChef: CHFQUEUE - Chefs in Queue
# Link         : https://www.codechef.com/LRNDSA02/problems/CHFQUEUE
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-19
# Description  :
# Status       : Time Limit Exceeded (34522405)
# Tags         : python, linear data structure, modular arithmetic
# Comment      :


from sys import exit, stdin, stdout

MOD = 1000000007

no_of_chiefs, no_of_seniority_levels = map(int, stdin.readline().split())
chiefs = [int(x) for x in stdin.readline().split()]
adepts = list(range(1, no_of_chiefs + 1))
adepts[-1] = None
fearfulness = 1
for i in range(no_of_chiefs - 2, -1, -1):
    seniority = chiefs[i]
    if seniority <= chiefs[i + 1]:
        idx = adepts[i + 1]
        while idx is not None and chiefs[idx] >= seniority:
            idx = adepts[idx]
        
        if idx is not None and chiefs[idx] < seniority:
            fearfulness = (fearfulness*(idx - i + 1)) % MOD
    else:
        fearfulness = (fearfulness << 1) % MOD

stdout.write(str(fearfulness) +'\n')
