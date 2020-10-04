# Project name : HackerRank: Lists
# Link         : https://www.hackerrank.com/challenges/python-lists/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-16
# Description  :
# Status       : Accepted (169212321)
# Tags         : python
# Comment      : 

if __name__ == '__main__':
    N = int(input())

    A = []

    for _ in range(N):
        operation_type, *params = input().split()

        if operation_type == 'insert':
            A.insert(int(params[0]), int(params[1]))
        elif operation_type == 'append':
            A.append(int(params[0]))
        elif operation_type == 'remove':
            A.remove(int(params[0]))
        elif operation_type == 'pop':
            A.pop()
        elif operation_type == 'print':
            print(A)
        elif operation_type == 'sort':
            A.sort()
        elif operation_type == 'reverse':
            A = A[::-1]
    