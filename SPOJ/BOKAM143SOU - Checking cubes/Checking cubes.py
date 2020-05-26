# Project name : SPOJ: BOKAM143SOU - Checking cubes.
# Author       : Wojciech Raszka
# Date created : 2019-03-22
# Description  :
# Status       : Accepted (23470768)
# Tags         : python, math, brute force
# Comment      : O(n^(5/3))

N = int(input())

cube_root = int(N**(1/3)) + 2
no_of_ways = 0
for i1 in range(cube_root):
    c1 = i1*i1*i1
    for i2 in range(i1, cube_root):
        c2 = c1 + i2*i2*i2
        for i3 in range(i2, cube_root):
            c3 = c2 + i3*i3*i3
            for i4 in range(i3, cube_root):
                c4 = c3 + i4*i4*i4
                for i5 in range(i4, cube_root):
                    c5 = c4 + i5*i5*i5
                    if c5 == N:
                        no_of_ways += 1

print(no_of_ways)
