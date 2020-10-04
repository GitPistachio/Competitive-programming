# Project name : HackerRank: Finding the percentage
# Link         : https://www.hackerrank.com/challenges/finding-the-percentage/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-15
# Description  :
# Status       : Accepted (169103368)
# Tags         : python
# Comment      : 

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    marks = student_marks[query_name]
    print('{:.2f}'.format(sum(marks)/len(marks)))
