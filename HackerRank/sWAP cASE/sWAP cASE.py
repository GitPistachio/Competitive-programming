# Project name : HackerRank: sWAP cASE
# Link         : https://www.hackerrank.com/challenges/swap-case/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-16
# Description  :
# Status       : Accepted (169213416)
# Tags         : python
# Comment      : 

def swap_case(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)