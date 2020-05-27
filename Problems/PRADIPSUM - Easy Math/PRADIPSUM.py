# Project name : SPOJ: PRADIPSUM - Easy Math
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-13
# Description  :
# Status       : Accepted (23915222)
# Tags         : python, arithmetic progression
# Comment      :

from sys import stdin, stdout

def sum_of_consecutive_numbers(a, b):
    if a > b:
        a, b = b, a

    return (a + b)/2*(b - a + 1)


for tokens in stdin:
    a, b = tokens.split()
    a, b = int(a), int(b)

    stdout.write('%d\n' %sum_of_consecutive_numbers(a, b))
