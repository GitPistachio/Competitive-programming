# Project name : SPOJ: ADV04J - Invisible point
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-21
# Description  :
# Status       : Accepted (23956428)
# Tags         : python, length of binary representation, integer sequence A070941 (OEIS)
# Comment      :

from sys import stdin, stdout

def lengthOfBinaryRepresentation(n):
    i = 0
    while n > 0:
        n = n >> 1
        i += 1

    return i

T = int(stdin.readline())

stdout.write('\n'.join([str(lengthOfBinaryRepresentation(((int(n) - 1) << 1) + 1)) for n in stdin.read().split()]))
stdout.write('\n')
