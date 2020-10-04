# Project name : HackerRank: Alphabet Rangoli
# Link         : https://www.hackerrank.com/challenges/alphabet-rangoli/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-16
# Description  :
# Status       : Accepted (169238377)
# Tags         : python, console pattern, rangoli
# Comment      : 

from string import ascii_lowercase

def print_rangoli(size):
    for i in range(size):
        right = ascii_lowercase[size - i - 1:size]
        letters = right[::-1][:-1] + right
        print('-'.join(letters).center((size << 2) - 3, '-'))
    
    for i in range(size - 2, -1, -1):
        right = ascii_lowercase[size - i - 1:size]
        letters = right[::-1][:-1] + right
        print('-'.join(letters).center((size << 2) - 3, '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)