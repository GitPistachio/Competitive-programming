# Project name : SPOJ: MFLAR10 - Flowers Flourish from France
# Author       : Wojciech Raszka
# Date created : 2019-03-17
# Description  :
# Status       : Accepted (23427291)
# Comment      :

import sys

for sentence in sys.stdin:
    if sentence != '*\n':
        if len(set(map(lambda x: x[0].lower() , sentence.split()))) == 1:
            print('Y')
        else:
            print('N')
    elif sentence != '\n':
        break
