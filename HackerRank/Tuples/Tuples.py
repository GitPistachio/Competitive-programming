# Project name : HackerRank: Tuples
# Link         : https://www.hackerrank.com/challenges/python-tuples/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-16
# Description  :
# Status       : Accepted (169212712)
# Tags         : python
# Comment      : 

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())

    print(hash(tuple(integer_list)))