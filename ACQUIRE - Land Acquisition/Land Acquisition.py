# Project name : SPOJ: ACQUIRE - Land Acquisition
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-05-31
# Description  :
# Status       : Accepted (23857981)
# Tags         : python, dynamic programming, convex hull trick, sweep line algorithm for the line segment intersection problem, pointer walk
# Comment      : 

from sys import stdin, stdout

MAX_COST = 1000000000000

def getDim(x):
    w, l = x.split()
    return (int(w), int(l))

n = int(stdin.readline())

rectangles = [getDim(x) for x in stdin]

rectangles.sort()
clean_rectangles = [rectangles[-1]]


for i in range(n - 2, -1, -1):
    if rectangles[i][1] > clean_rectangles[-1][1]:
        clean_rectangles.append(rectangles[i])

def minCostNaive(rectangles):
    '''Time complexity O(n^2)'''

    n = len(rectangles)
    cost = [0]*(n + 1)

    for i in range(1, n + 1):
        cost[i] = MAX_COST
        for j in range(i):
            cost[i] = min(cost[i], cost[j] + rectangles[i - 1][0]*rectangles[j][1])

    return cost[n]

def minCost(rectangles):
    '''Time complexity O(n)'''

    n = len(rectangles)
    cost = [0]*(n + 1)
    lines = []

    lines.append((rectangles[0][1], 0, 0))

    inv = 0
    no_of_lines = 1
    for i in range(1, n + 1):
        while inv < no_of_lines - 1:
            if lines[inv + 1][2] <= rectangles[i - 1][0]:
                inv += 1
            else:
                break

        cost[i] = lines[inv][0]*rectangles[i - 1][0] + lines[inv][1]

        if i < n:
            while True:
                intersection_point = float(cost[i] - lines[-1][1])/(lines[-1][0] - rectangles[i][1])
                if no_of_lines > 1:
                    if intersection_point < lines[-1][2]:
                        lines.pop()
                        no_of_lines -= 1
                    else:
                        lines.append((rectangles[i][1], cost[i], intersection_point))
                        no_of_lines += 1
                        break
                else:
                    lines.append((rectangles[i][1], cost[i], intersection_point))
                    no_of_lines += 1
                    break

    return cost[n]

clean_rectangles.reverse()
stdout.write('%d\n' % minCost(clean_rectangles))

#stdout.write('%d\n' % minCostNaive(clean_rectangles))
