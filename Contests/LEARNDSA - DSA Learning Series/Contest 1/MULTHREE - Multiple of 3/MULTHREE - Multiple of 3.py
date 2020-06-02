# Project name : CodeChef: MULTHREE - Multiple of 3
# Link         : https://www.codechef.com/LRNDSA01/problems/MULTHREE
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio
# Date created : 2020-06-02
# Description  :
# Status       : Accepted (33577734)
# Tags         : python, modular arithmetic, divisibility by 3, number theory
# Comment      :

from sys import stdin, stdout


def rest(n):
    q = n//4
    r = n % 4

    if r > 0:
        if r > 1:
            if r > 2:
                return 20*q + 14

            return 20*q + 6

        return 20*q + 2
    
    return 20*q


def solve(k, d0, d1):
    x = d0 + d1
    sum_of_digits = x
    
    factor = 1
    for i in range(2, k):
        di = (factor*x) % 10
        if di == 0:
            break
        elif di == 2:
            sum_of_digits += rest(k - i)
            break
        
        sum_of_digits += di
        factor <<= 1
    
    return sum_of_digits

no_of_test_cases = int(stdin.readline())

for _ in range(no_of_test_cases):
    k, d0, d1 = map(int, stdin.readline().split())
    sum_of_digits = solve(k, d0, d1)
    if sum_of_digits % 3 == 0:
        stdout.write("YES\n")
    else:
        stdout.write("NO\n")

