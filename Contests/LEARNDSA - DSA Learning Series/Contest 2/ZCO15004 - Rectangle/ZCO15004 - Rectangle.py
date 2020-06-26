# Project name : CodeChef: ZCO15004 - Rectangle
# Link         : https://www.codechef.com/LRNDSA02/problems/ZCO15004
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-19
# Description  :
# Status       : Accepted (34545596)
# Tags         : python, linear data structure, zonal computing olympiad 2015, area of rectangle, Barbay-Fischer-Navarro sequential algorithm, all nerest smaller values, maximum rectangle under the histogram
# Comment      :

from sys import exit, stdin, stdout


def maxRectAreaUnderHist(hist):
    n = len(hist)
    P = [0]*n
    max_area = 0
    # print(hist)
    for i in range(n):
        j = i - 1
        # print(i, j, hist[i], hist[j])
        while j >= 0 and hist[j] >= hist[i]:
            area = hist[j]*(i - P[j]) # should be hist[j]*(i - P[j] - 1), -1 is lost for the problem
            if area > max_area:
                max_area = area
            # print('  ', i, j, P[j], hist[i], hist[j], area)
            j = P[j]
        
        P[i] = j
    
    j = n - 1
    while j >= 0:
        area = hist[j]*(n - P[j] - 1)
        # print('  ', i, j, P[j], hist[i], hist[j], area)
        if area > max_area:
            max_area = area
        j = P[j]
    
    return max_area
    

REGION_HEIGHT = 500
REGION_WIDTH = 100000
no_of_points = int(stdin.readline())
points = [REGION_HEIGHT]*(REGION_WIDTH + 1)
points[0] = 0
for _ in range(no_of_points):
    x, y = map(int, stdin.readline().split())
    #x += 1
    if points[x] > y:
        points[x] = y

#print(points)
max_area = maxRectAreaUnderHist(points)


stdout.write(str(max_area) + '\n')

