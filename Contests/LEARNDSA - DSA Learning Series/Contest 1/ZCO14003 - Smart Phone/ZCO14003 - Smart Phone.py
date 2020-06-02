# Project name : CodeChef: ZCO14003 - Smart Phone
# Link         : https://www.codechef.com/LRNDSA01/problems/ZCO14003
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio
# Date created : 2020-06-02
# Description  :
# Status       : Accepted (33573071)
# Tags         : python
# Comment      :

from sys import stdin, stdout


no_of_potential_customers = int(stdin.readline())

budgets = sorted([int(x) for x in stdin])
maximum_possible_revenue = 0
for i in range(no_of_potential_customers):
    possible_revenue = budgets[i]*(no_of_potential_customers - i)
    if possible_revenue > maximum_possible_revenue:
        maximum_possible_revenue = possible_revenue

stdout.write(str(maximum_possible_revenue))