# Project name : HackerRank: String Split and Join
# Link         : https://www.hackerrank.com/challenges/python-string-split-and-join/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-16
# Description  :
# Status       : Accepted (169213696)
# Tags         : python
# Comment      : 

def split_and_join(line):
    return '-'.join(line.split(' '))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
