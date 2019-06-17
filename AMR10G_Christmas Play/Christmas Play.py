# Project name : SPOJ: AMR10G - Christmas Play
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-03-08
# Description  :
# Status       : Accepted (23367585)
# Tags         : python
# Comment      :

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    K -= 1

    if K > 0:
        smallest_heights_diff = 1000000000
        heights = sorted(map(int, input().split()))

        for i in range(len(heights) - K):
            if heights[i + K] - heights[i] < smallest_heights_diff:
                smallest_heights_diff = heights[i + K] - heights[i]
    else:
        smallest_heights_diff = 0
        input()

    print(smallest_heights_diff)
