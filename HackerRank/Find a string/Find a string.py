# Project name : HackerRank: Find a string
# Link         : https://www.hackerrank.com/challenges/find-a-string/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-16
# Description  :
# Status       : Accepted (169215848)
# Tags         : python
# Comment      : 

def count_substring(string, sub_string):
    cnt = 0
    pos = 0
    while True:
        pos = string.find(sub_string, pos)
        if pos == -1:
            break
        
        pos += 1
        cnt += 1
    
    return cnt

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)