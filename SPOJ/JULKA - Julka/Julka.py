# Project name : SPOJ: JULKA - Julka
# Link         : https://www.spoj.com/problems/JULKA/
# Try it on    : https://ideone.com/3iZ5ff
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-05-26
# Description  :
# Status       : Accepted (26042577)
# Tags         : python, big numbers
# Comment      :

from sys import stdin, stdout

NO_OF_TESTS = 10

for _ in range(NO_OF_TESTS):
    z = int(stdin.readline())
    d =  int(stdin.readline())
    y = (z - d)//2
    x = z - y
    
    stdout.write("{}\n{}\n".format(x, y))