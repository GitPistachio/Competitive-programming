# Project name : SPOJ: Even numbers
# Author       : Wojciech Raszka
# Date created : 2019-02-10
# Description  :
# Status       : Accepted (23204625)
# Comment      :


N = int(raw_input())

for i in range(N):
    n = int(input())
    if (n % 2 == 0):
        print int(bin(n)[:1:-1], 2)
    else:
        print n
