# Project name : SPOJ: HYDRO - Hydroelectric dams
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-27
# Description  :
# Status       : Accepted (23693275)
# Tags         : python, histogram, maximum flooded area
# Comment      : O(n)

import sys

T = int(sys.stdin.readline())

while T > 0:
    n = int(sys.stdin.readline())
    H = [int(x) for x in sys.stdin.readline().split()]

    WH = []
    start = 0
    while start < n:
        if H[start] > 0:
            WH.append([start, H[start], 0])
            break
        start += 1

    k = 0 # no of dams in stack
    frozen_no_of_dams = 1
    for i in range(start + 1, n):
        h = H[i]
        if h > 0:
            d = [i, h, 0]
            sum_of_flooded_dams = 0
            while k >= frozen_no_of_dams:
                if WH[k][1] <= h:
                    pd = WH.pop()
                    sum_of_flooded_dams += pd[1] + pd[2]
                    k -= 1
                else:
                    break

            d[2] = sum_of_flooded_dams
            WH.append(d)
            k += 1
            if h > WH[frozen_no_of_dams - 1][1]:
                frozen_no_of_dams = k + 1


    max_water_hold = 0
    while k > 0:
        h = min(WH[k][1], WH[k - 1][1])
        width = WH[k][0] - WH[k - 1][0] - 1
        max_water_hold += h*width - WH[k][2]
        k -= 1

    sys.stdout.write("%d\n" % max_water_hold)
    T -= 1
