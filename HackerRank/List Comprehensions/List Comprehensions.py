# Project name : HackerRank: List Comprehensions
# Link         : https://www.hackerrank.com/challenges/list-comprehensions/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-15
# Description  :
# Status       : Accepted (169100749)
# Tags         : python
# Comment      : 


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    points = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]

    points = list(filter(lambda p: sum(p) != n, points))
    print(points)
