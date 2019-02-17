# Project name : SPOJ: Game store
# Author       : Wojciech Raszka
# Date created : 2019-02-09
# Description  :
# Status       : Accepted (23206442)
# Comment      :

N = int(input())

for n in range(N):
    x, y = input().split()
    x, y = int(x), int(y)

    if x == 0 and y == 0:
        print(0)
    elif x == 1 and y == 1:
        print(1)
    elif x == y:
        print(2*x -(x % 2))
    elif y == x - 2:
        print(2*x - 2 - (x % 2))
    else:
        print("No Number")
