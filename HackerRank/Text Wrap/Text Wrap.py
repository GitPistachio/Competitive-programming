# Project name : HackerRank: Text Wrap
# Link         : https://www.hackerrank.com/challenges/text-wrap/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-16
# Description  :
# Status       : Accepted (169232587)
# Tags         : python
# Comment      : 

import textwrap

def wrap(string, max_width):
    return '\n'.join([string[i:i + max_width] for i in range(0, len(string), max_width)])

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)