# Project name : SPOJ: TMUL - Not So Fast Multiplication
# Author       : Wojciech Raszka
# E-mail       : gitpistachi@gmail.com
# Date created : 2019-06-02
# Description  :
# Status       : Accepted (23866368)
# Tags         : python
# Comment      :

from sys import stdin, stdout

T = int(stdin.readline())

stdout.write('\n'.join(map(lambda x: str(eval(x.replace(' ', '*'))), stdin)))
stdout.write('\n')
