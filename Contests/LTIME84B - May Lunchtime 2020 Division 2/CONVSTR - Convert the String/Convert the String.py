# Project name : CodeChef: CONVSTR - Convert the String
# Link         : https://www.codechef.com/LTIME84B/problems/CONVSTR
# Try it on    : https://ideone.com/WXkNFQ
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-05-30
# Description  :
# Status       : Accepted(33488806)
# Tags         : python, string manipulation
# Comment      : 100

from sys import stdin, stdout


def solveOneStep(n, A, B):
    c = ''
    for a, b in zip(A, B):
        if a != b:
            if b > c:
                c = b

    if c == '':
        return []

    is_c_found_in_a = False
    S = []
    for i in range(n):
        if B[i] == c and A[i] != B[i]:
            if A[i] < c:
                return -1
            S.append(i)

        if not is_c_found_in_a and A[i] == c:
            is_c_found_in_a = True
            S.append(i)

    if is_c_found_in_a:
        for i in S:
            A[i] = c
        return S
    else:
        return -1

no_of_test_cases = int(stdin.readline())

for _ in range(no_of_test_cases):
    n = int(stdin.readline())
    A = list(stdin.readline().strip())
    B = list(stdin.readline().strip())
    k = 0
    output = ''
    while True:
        S = solveOneStep(n, A, B)
        if S == -1:
            stdout.write("-1\n")
            break
        elif S == []:
            stdout.write("{}\n".format(k))
            stdout.write(output)
            break
        else:
            k += 1
            output += str(len(S)) + ' ' + ' '.join(map(str, S)) + '\n'
