# Project name : HackerRank: Day 2: Operators
# Link         : https://www.hackerrank.com/challenges/30-operators/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-19
# Description  :
# Status       : Accepted (164894056)
# Tags         : python
# Comment      : 

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost*tip_percent/100.0
    tax = meal_cost*tax_percent/100.0
    return round(meal_cost + tip + tax)

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    total_meal_cost = solve(meal_cost, tip_percent, tax_percent)
    print(total_meal_cost)
