# Project name : SPOJ: KOPC12A - K12 - Building Construction
# Link         : https://www.spoj.com/problems/KOPC12A/
# Try it on    : https://ideone.com/JgLE9N
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-05-25
# Description  :
# Status       : Accepted (26037033)
# Tags         : python, weakly unimodal function, ternary search algorithm
# Comment      :

from sys import stdin, stdout


def reconstructionCost(h, H, C):
    """Calculate the cost of re-costruction. Function is weakly unimodal, thus it is applicable to ternary search."""
    cost = 0
    for i in range(len(H)):
        cost += abs(H[i] - h)*C[i]
    
    return cost


def ternarySearch(left, right, f, *args):
    """Find minimum of weakly unimodal function by ternary search."""
    while right > left:
        one_third = (right - left)//3
        left_third = left + one_third
        right_third = right - one_third
        if f(left_third, *args) < f(right_third, *args):
            right = right_third - 1
        else:
            left = left_third + 1
    
    return left
    

if __name__ == "__main__":
    no_of_test_cases = int(stdin.readline())
    for _ in range(no_of_test_cases):
        no_of_buildings = int(stdin.readline())
        H = [int(h) for h in stdin.readline().split()]
        C = [int(c) for c in stdin.readline().split()]
        h = ternarySearch(min(H), max(H), reconstructionCost, H, C)
        stdout.write("{}\n".format(reconstructionCost(h, H, C)))