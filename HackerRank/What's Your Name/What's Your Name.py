# Project name : HackerRank: What's Your Name?
# Link         : https://www.hackerrank.com/challenges/python-string-split-and-join/submissions/code/169213696
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-16
# Description  :
# Status       : Accepted (169213696)
# Tags         : python
# Comment      : 

def print_full_name(a, b):
    print("Hello {} {}! You just delved into python.".format(a, b))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
