# Project name : CodeChef: ZCO12002 - Wormholes
# Link         : https://www.codechef.com/LRNDSA02/problems/ZCO12002
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-19
# Description  :
# Status       : Accepted (34526283)
# Tags         : python, linear data structure, zonal computing olympiad 2012, floor binary search, ceil binary search
# Comment      :


from sys import exit, stdin, stdout


def floorBinarySearch(A, low, high, x):
    if x >= A[high]:
        return high

    while low <= high:
        mid = low + (high - low)//2
        
        if x < A[mid]:
            if mid > 0 and A[mid - 1] <= x: 
                return mid - 1

            high = mid - 1
        elif x > A[mid]:
            low = mid + 1
        else:
            return mid
    
    return -1


def ceilBinarySearch(A, low, high, x):
    if x <= A[low]:
        return low

    n = high - low + 1
    while low <= high:
        mid = low + (high - low)//2
        
        if x < A[mid]:
            high = mid - 1
        elif x > A[mid]:
            if mid + 1 < n and A[mid + 1] >= x: 
                return mid + 1
            low = mid + 1
        else:
            return mid
    
    return -1
    
no_of_contests, no_of_v_wormholes, no_of_w_wormholes = map(int, stdin.readline().split())
contests_intervals = [map(int, stdin.readline().split()) for _ in range(no_of_contests)]
v_wormholes = sorted(map(int, stdin.readline().split()))
w_wormholes = sorted(map(int, stdin.readline().split()))

min_time_needed = 1000001
for a, b in contests_intervals:
    if b - a + 1 < min_time_needed:
        v_idx = floorBinarySearch(v_wormholes, 0, no_of_v_wormholes - 1, a)
        if v_idx >= 0:
            v = v_wormholes[v_idx]
            if b - v + 1 < min_time_needed:
                w_idx = ceilBinarySearch(w_wormholes, 0, no_of_w_wormholes - 1, b)
                if w_idx >= 0:
                    w = w_wormholes[w_idx]
                    if w - v + 1 < min_time_needed:
                        min_time_needed = w - v + 1

stdout.write(str(min_time_needed) +'\n')
