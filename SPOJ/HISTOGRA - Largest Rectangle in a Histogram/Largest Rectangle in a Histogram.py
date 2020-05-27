# Project name : SPOJ: HISTOGRA - Largest Rectangle in a Histogram
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-26
# Description  :
# Status       : Accepted (23689892)
# Tags         : python, rectangle, histogram, largest rectangle under histogram
# Comment      :


def largestRectangularArea(H):
    stack = []

    max_area = 0
    i = 0
    n = len(H)
    while i < n:
        if (not stack) or (H[stack[-1]] <= H[i]):
            stack.append(i)
            i += 1
        else:
            top = stack.pop()
            if stack:
                area = H[top]*(i - stack[-1] - 1)
            else:
                area = H[top]*i

            max_area = max(max_area, area)

    while stack:
        top = stack.pop()

        if stack:
            area = H[top]*(i - stack[-1] - 1)
        else:
            area = H[top]*i

        max_area = max(max_area, area)

    return max_area


while True:
    H = [int(x) for x in input().split()]

    if len(H) == 1 and H[0] == 0:
        break

    print(largestRectangularArea(H[1:]))
