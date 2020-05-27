# Project name : SPOJ: Sum of digits
# Author       : Wojciech Raszka
# Date created : 2019-02-06
# Description  :
# Status       : Accepted (23186673)
# Comment      :

T = int(input())

for t in range(T):
    N = int(input())

    hotness_levels_of_men = sorted(map(int, input().split(' ')))
    hotness_levels_of_women = sorted(map(int, input().split(' ')))

    sum_of_hotness_bonds = 0
    for i in range(N):
        sum_of_hotness_bonds += hotness_levels_of_men[i]*hotness_levels_of_women[i]
    print(sum_of_hotness_bonds)
