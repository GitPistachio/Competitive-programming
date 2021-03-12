# Project name : SPOJ: KNJIGE - KNJIGE
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-03-12
# Description  :
# Status       : Accepted (27545906)
# Tags         : python, restricted sort
# Comment      : 

from sys import stdin, stdout
 
no_of_books = int(stdin.readline())
books = [int(stdin.readline()) for _ in range(no_of_books)]
 
last_value = no_of_books + 1
no_of_steps = no_of_books
for value in books[::-1]:
    if value == last_value - 1:
        no_of_steps -= 1
        last_value = value
 
stdout.write('{}\n'.format(no_of_steps))