# Project name : SPOJ: NSORT - Name Sorting
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-03-11
# Description  :
# Status       : Accepted (27542759)
# Tags         : python, dynamic programming, game
# Comment      : Theoretically, you have three options but if you think about it a litte you see that it is always good to be on air. Thus every time when you can you should step on air as well as you should start on air. Thus it reduces possible ways, because you alwasy be on air + fire or air + water or just air and you die. So it is beter to reduce tree ways to two: air + fire and air + water and count how many pair you can be on plus at the end you can stay on air.

from sys import stdin, stdout

solutions = {}

def solve(H, A):
    if (H, A) in solutions:
        return solutions[(H, A)]
    
    result = 0
    if H > 17:
        if A > 8:
            # You can choose: be on are then of fire or be on air and then on water
            fire = solve(H - 17, A + 7)
            water = solve(H - 2, A - 8)
            
            result = max(fire, water) + 2
        elif A > 0:
            # You cannot survive to be on air then on water but you can survive be on air then of fire
            fire = solve(H - 17, A + 7) + 2
            result = fire
    elif H > 2:
        if A > 8:
            # You cannot survive to be on air then on water but you can survivie to be on air then of water
            water = solve(H - 2, A - 8) + 2
            result = water
        elif A > 0:
            # You only can survive once on air
            result = 1
    elif H > 0 and A > 0:
        # You only can survive one on air
        result = 1

    solutions[(H, A)] = result
    return result

    
no_of_test_cases = int(stdin.readline())
for _ in range(no_of_test_cases):
    H, A = map(int, stdin.readline().split())
    max_time_of_survival = solve(H, A)
    stdout.write('{}\n'.format(max_time_of_survival))
    