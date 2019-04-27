# Project name : SPOJ: EDIST - Edit distance
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmial.com
# Date created : 2019-04-26
# Description  :
# Status       : Accepted (23689322)
# Tags         : python, edit distance, the Levenshtein distance
# Comment      : O(n*m)

def editDistance(s1, s2):
    m = len(s1)
    n = len(s2)
    d = [[0 for x in range(n + 1)] for x in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                d[i][j] = j
            elif j == 0:
                d[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = 1 + min(d[i][j - 1], d[i - 1][j], d[i - 1][j - 1])

    return d[m][n]

T = int(raw_input())

while T > 0:
    s1 = raw_input()
    s2 = raw_input()

    print editDistance(s1, s2)

    T -= 1
