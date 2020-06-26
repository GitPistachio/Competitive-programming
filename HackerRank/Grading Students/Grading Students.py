# Project name : HackerRank: Grading Students
# Link         : https://www.hackerrank.com/challenges/grading/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-25
# Description  :
# Status       : Accepted (165649216)
# Tags         : python
# Comment      : 

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):

    rounded_grades = grades.copy()
    for i in range(len(grades)):
        if rounded_grades[i] >= 38 and rounded_grades[i] % 5 >= 3:
            rounded_grades[i] += 5 - (rounded_grades[i] % 5)
    
    return rounded_grades

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
