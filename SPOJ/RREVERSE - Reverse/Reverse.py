# Project name : SPOJ: RREVERSE - Reverse
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-14
# Description  :
# Status       : Accepted (23631652)
# Tags         : python
# Comment      :

import sys

for token in sys.stdin:
    print(int(token[::-1]))
