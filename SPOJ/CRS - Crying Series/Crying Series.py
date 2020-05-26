# Project name : SPOJ: CRS - Crying Series
# Author       : Wojciech Raszka
# Date created : 2019-03-09
# Description  :
# Status       : Accepted (23373929)
# Tags         : python
# Comment      :

import sys

for line in sys.stdin:
    n = int(line)

    F = (n + 1)//2
    if n % 2:
        F = -F

    print(F)
