# Project name : SPOJ: VPL0_E - External Sequence
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-05-12
# Description  :
# Status       : Accepted (23754842)
# Tags         : python, number theory, integer sequence A005150 (OEIS), look and say sequence
# Comment      : 173

def a(n):
    if n < 1:
        return '1'
    t = ''
    f = 0
    l = ''
    for d in a(n - 1):
        if l != d:
            t += (str(f) + l)*min(1, f)
            f = 0
        f += 1
        l = d
    return t + str(f) + l
for t in range(int(input())):
    print('Scenario #%d: %s' % (t + 1, a(int(input()))))
