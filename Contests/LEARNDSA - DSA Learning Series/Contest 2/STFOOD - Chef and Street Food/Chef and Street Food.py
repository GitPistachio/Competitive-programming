# Project name : CodeChef: STFOOD - Chef and Street Food
# Link         : https://www.codechef.com/LRNDSA02/problems/STFOOD
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-19
# Description  :
# Status       : Accepted (34521593)
# Tags         : python, linear data structure
# Comment      :

from sys import exit, stdin, stdout


no_of_test_cases = int(stdin.readline())
for _ in range(no_of_test_cases):
    no_of_food_types = int(stdin.readline())
    max_profit = 0
    for s, p, v in [map(int, stdin.readline().split()) for _ in range(no_of_food_types)]:
        profit = (p//(s + 1))*v
        if profit > max_profit:
            max_profit = profit
    
    stdout.write(str(max_profit) + '\n')
