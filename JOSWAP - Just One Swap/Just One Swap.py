# Project name : SPOJ: JOSWAP - Just One Swap
# Author       : Wojciech Raszka
# Date created : 2019-03-24
# Description  :
# Status       : Accepted (23479022)
# Tags         : python, sorting, group by, count
# Comment      :

from sys import stdin, stdout
from itertools import groupby

T = int(input())

for t in range(T):
    N = int(input())
    no_of_comb = 0
    no_of_elements = 0
    possible_to_swap_same = False
    for x, y in groupby(sorted(input().split())):
        y = len(list(y))
        no_of_comb += no_of_elements*y
        no_of_elements += y
        if y > 1:
            possible_to_swap_same = True

    if possible_to_swap_same:
        no_of_comb += 1

    print(no_of_comb)
