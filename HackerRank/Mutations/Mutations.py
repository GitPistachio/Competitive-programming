# Project name : HackerRank: Mutations
# Link         : https://www.hackerrank.com/challenges/python-mutations/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-16
# Description  :
# Status       : Accepted (169214742)
# Tags         : python
# Comment      : 

def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    return ''.join(l)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)