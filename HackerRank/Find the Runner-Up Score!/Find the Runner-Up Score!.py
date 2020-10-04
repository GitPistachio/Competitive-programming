# Project name : HackerRank: Find the Runner-Up Score!
# Link         : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-15
# Description  :
# Status       : Accepted (169101645)
# Tags         : python
# Comment      : 

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    max_a = -100
    second_max_a = -100

    for a in arr:
        if a > max_a:
            second_max_a = max_a
            max_a = a
        elif a > second_max_a and a != max_a:
            second_max_a = a
    
    print(second_max_a)
  