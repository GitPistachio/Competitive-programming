# Project name : HackerRank: String Validators
# Link         : https://www.hackerrank.com/challenges/string-validators/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-16
# Description  :
# Status       : Accepted (169226631)
# Tags         : python
# Comment      : 

if __name__ == '__main__':
    s = input()
    
    stats = [False]*5
    for c in s:
        if c.isalnum():
            stats[0] = True
        
        if c.isalpha():
            stats[1] = True
        
        if c.isdigit():
            stats[2] = True
        
        if c.islower():
            stats[3] = True
        
        if c.isupper():
            stats[4] = True
    
    for stat in stats:
        print(stat)
    
