# Project name : CodeChef: PRICECON - Chef and Price Control
# Link         : https://www.codechef.com/JUNE20B/problems/PRICECON
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-06-05
# Description  :
# Status       : Accepted (33700367)
# Tags         : python
# Comment      : 100

from sys import stdin, stdout

no_of_test_cases = int(stdin.readline())

for _ in range(no_of_test_cases):
    no_of_items, max_price = map(int, stdin.readline().split())
    max_revenue = sum(map(lambda x: int(x) - min(max_price, int(x)), stdin.readline().split()))
    stdout.write(str(max_revenue) + "\n")
