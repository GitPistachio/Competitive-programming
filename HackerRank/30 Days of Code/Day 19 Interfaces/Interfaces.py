# Project name : HackerRank: Day 19: Interfaces
# Link         : https://www.hackerrank.com/challenges/30-interfaces/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-10
# Description  :
# Status       : Accepted (168240280)
# Tags         : python
# Comment      : 

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        divisor_sum = 0
        i = 1
        while i <= n:
            if n % i == 0:
                divisor_sum += i
            
            i += 1

        return divisor_sum


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)   