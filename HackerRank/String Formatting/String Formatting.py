# Project name : HackerRank: String Formatting
# Link         : https://www.hackerrank.com/challenges/python-string-formatting/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-16
# Description  :
# Status       : Accepted (169238377)
# Tags         : python
# Comment      : 

def print_formatted(number):
    s = len(bin(number)) - 2
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = bin(i)[2:]

        print(decimal.rjust(s), octal.rjust(s), hexadecimal.rjust(s), binary.rjust(s))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)