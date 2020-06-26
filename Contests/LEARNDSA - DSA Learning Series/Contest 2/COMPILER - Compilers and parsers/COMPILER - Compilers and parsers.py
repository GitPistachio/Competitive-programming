# Project name : CodeChef: COMPILER - Compilers and parsers
# Link         : https://www.codechef.com/LRNDSA02/problems/COMPILER
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-19
# Description  :
# Status       : Accepted (34521822)
# Tags         : python, linear data structure, parser
# Comment      :

from sys import exit, stdin, stdout
from collections import deque 


def solve(expression):
    stack = deque()
    no_of_valid_expr = 0
    no_of_valid_expr_in_sgm = 0
    for symbol in expression:
        if symbol == '<':
            stack.append(symbol)
        else:
            if not stack or stack.pop() != '<':
                return no_of_valid_expr

            if not stack:
                no_of_valid_expr += no_of_valid_expr_in_sgm + 2
                no_of_valid_expr_in_sgm = 0
            else:
                no_of_valid_expr_in_sgm += 2
    
    return no_of_valid_expr

no_of_test_cases = int(stdin.readline())
for _ in range(no_of_test_cases):
    expression = stdin.readline().strip()
    no_of_valid_expr = solve(expression)
    stdout.write(str(no_of_valid_expr) + '\n')
