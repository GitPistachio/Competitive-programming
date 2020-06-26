# Project name : CodeChef: PSHOT - Penalty Shoot-Out II
# Link         : https://www.codechef.com/LRNDSA02/problems/PSHOT
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-19
# Description  :
# Status       : Accepted (34521696)
# Tags         : python, game theory, football penalty kicks
# Comment      :

from sys import exit, stdin, stdout


def minNoOfShots(no_of_shots_by_one_team, shots):
    diff_in_no_of_goals = 0
    for i in range(no_of_shots_by_one_team):
        if shots[2*i] == '1':
            diff_in_no_of_goals += 1
            if no_of_shots_by_one_team - i < diff_in_no_of_goals:
                return 2*i + 1
        else:
            if no_of_shots_by_one_team - i  - 1 < -diff_in_no_of_goals:
                return 2*i + 1
        
        if shots[2*i + 1] == '1':
            diff_in_no_of_goals -= 1
            if no_of_shots_by_one_team - i  -  1 < -diff_in_no_of_goals:
                return 2*(i + 1)
        else:
            if no_of_shots_by_one_team - i  - 1 < diff_in_no_of_goals:
                return 2*(i + 1)
    
    return 2*no_of_shots_by_one_team


no_of_test_cases = int(stdin.readline())
for _ in range(no_of_test_cases):
    no_of_shots_by_one_team = int(stdin.readline())
    shots = stdin.readline()
    min_no_of_shots = minNoOfShots(no_of_shots_by_one_team, shots)
    
    stdout.write(str(min_no_of_shots) + '\n')
