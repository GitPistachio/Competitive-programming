# Project name : CodeChef: STUPMACH - Stupid Machine
# Link         : https://www.codechef.com/LRNDSA02/problems/STUPMACH
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-19
# Description  :
# Status       : Accepted (34521755)
# Tags         : python, linear data structure
# Comment      :

from sys import exit, stdin, stdout


no_of_test_cases = int(stdin.readline())
for _ in range(no_of_test_cases):
    no_of_boxes = int(stdin.readline())
    S = [int(x) for x in stdin.readline().split()]
    
    moving_min = S[0]
    max_no_of_tokens = 0
    for i in range(1, no_of_boxes):
        if S[i] < moving_min:
            max_no_of_tokens += i*(moving_min - S[i])
            moving_min = S[i]
    
    max_no_of_tokens += no_of_boxes*moving_min
    
    stdout.write(str(max_no_of_tokens) + '\n')
