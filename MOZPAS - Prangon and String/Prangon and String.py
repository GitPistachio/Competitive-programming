# Project name : SPOJ: MOZPAS - Prangon and String
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-21
# Description  :
# Status       : Accepted (23669618)
# Tags         : python
# Comment      :

import string
n, m = map(int, input().split())


prangon = ''
for l in string.ascii_letters:

    prangon += l*min(n - len(prangon), m)

    if len(prangon) == n:
        print(prangon)
        break
