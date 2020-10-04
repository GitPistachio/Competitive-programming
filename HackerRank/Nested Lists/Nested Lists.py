# Project name : HackerRank: Nested Lists
# Link         : https://www.hackerrank.com/challenges/nested-list/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-15
# Description  :
# Status       : Accepted (169103056)
# Tags         : python
# Comment      : 

if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
    
    min_score = 100
    second_min_score = 100

    for name, score in records:
        if score < min_score:
            second_min_score = min_score
            min_score = score
        elif score < second_min_score and score != min_score:
            second_min_score = score
    
    sucker_names = []

    for name, score in records:
        if score == second_min_score:
            sucker_names.append(name)
    
    for name in sorted(sucker_names):
        print(name)