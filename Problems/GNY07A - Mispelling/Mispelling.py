# Project name : SPOJ: GNY07A - Mispelling
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-03-27
# Description  :
# Status       : Accepted (23506270)
# Tags         : python
# Comment      :

T = int(input())

for t in range(1, T + 1):
    m, word = input().split()
    m = int(m)

    word = word[:m - 1] + word[m:]

    print(t, word)
