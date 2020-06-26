# Project name : CodeChef: ZCO12001 - Matched Brackets
# Link         : https://www.codechef.com/LRNDSA02/problems/ZCO12001
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-19
# Description  :
# Status       : Accepted (34521926)
# Tags         : python, linear data structure, zonal computing olympiad 2012, infix expression
# Comment      :

from sys import exit, stdin, stdout
from collections import deque 


OPENING_BRACKET = '1'
CLOSING_BRACKET = '2'

def solve(expr):
    stack = deque()
    nesting_depth = 0
    max_nesting_depth = 0
    max_nesting_depth_1st_occ = 0
    sequence_len = 0
    max_sequence_len = 0
    max_sequence_len_1st_occ = 0
    
    for i in range(len(expr)):
        symbol = expr[i]
        if symbol == OPENING_BRACKET:
            if stack:
                stack.append((symbol, stack[-1][1] + 1, i))
            else:
                stack.append((symbol, 0, i))
        elif symbol == CLOSING_BRACKET:
            if not stack:
                raise Exception('Expression is not well-bracked')
            
            last_symbol, last_depth, last_position = stack.pop()
            if last_symbol != OPENING_BRACKET:
                raise Exception('Expression is not well-bracked')
            
            if last_depth > nesting_depth:
                nesting_depth = last_depth
                if max_nesting_depth < nesting_depth:
                    max_nesting_depth = nesting_depth
                    max_nesting_depth_1st_occ = last_position

            sequence_len += 2
            if not stack:
                if max_sequence_len < sequence_len:
                    max_sequence_len = sequence_len
                    max_sequence_len_1st_occ = last_position

                nesting_depth = 0
                sequence_len = 0

    
    return (max_nesting_depth + 1, max_nesting_depth_1st_occ + 1, max_sequence_len, max_sequence_len_1st_occ + 1)


no_of_brackets = int(stdin.readline())
expr = stdin.readline().strip()
max_nesting_depth, max_nesting_depth_1st_occ, max_sequence_len, max_sequence_len_1st_occ = solve(expr.replace(' ', ''))
stdout.write(str(max_nesting_depth) + ' ' + str(max_nesting_depth_1st_occ) + ' ' + str(max_sequence_len) + ' ' + str(max_sequence_len_1st_occ) +'\n')
