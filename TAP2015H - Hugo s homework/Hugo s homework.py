# Project name : SPOJ: TAP2015H - Hugo s homework
# Author       : Wojciech Raszka
# Date created : 2019-02-20
# Description  :
# Status       : Accepted (23268725)
# Tags         : python
# Comment      :

def substraction(n):
    if n == 0:
        return 0
    else:
        return 1 + substraction(n - int(''.join(sorted(str(n)))))

import sys

for line in sys.stdin:
    n = int(line)
    print(substraction(n))
