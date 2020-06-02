# Project name : CodeChef: CARVANS - Carvans
# Link         : https://www.codechef.com/LRNDSA01/problems/CARVANS
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio
# Date created : 2020-06-02
# Description  :
# Status       : Accepted (33570900)
# Tags         : python
# Comment      :

from sys import stdin, stdout
from functools import reduce


def solve(result, car_speed):
    if car_speed <= result[0]:
        return (car_speed, result[1] + 1)
    else:
        return result
    

MAX_SPEED = 2147483647 # max 32 bit signed int
no_of_test_cases = int(stdin.readline())

for _ in range(no_of_test_cases):
    n = int(stdin.readline())
    A = map(int, stdin.readline().split())
    no_of_cars_with_max_speed = reduce(solve, A, (MAX_SPEED, 0))[1]
    stdout.write(str(no_of_cars_with_max_speed) + "\n")
