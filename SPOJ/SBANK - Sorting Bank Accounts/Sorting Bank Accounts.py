# Project name : SPOJ: SBANK - Sorting Bank Accounts
# Author       : Wojciech Raszka
# Date created : 2019-03-15
# Description  :
# Status       : Accepted (23420527)
# Tags         : python, sorting, group by
# Comment      : O(nlogn)

import sys
from itertools import groupby

T = int(sys.stdin.readline())

for t in range(T):
    n = int(sys.stdin.readline())
    bank_accounts = sorted([sys.stdin.readline().rstrip() for i in range(n)])
    sys.stdout.write('\n'.join([k + " " + str(len(list(g))) for k, g in groupby(bank_accounts)]) + "\n")

    if t + 1 < T:
        sys.stdout.write("\n")
        sys.stdin.readline()
