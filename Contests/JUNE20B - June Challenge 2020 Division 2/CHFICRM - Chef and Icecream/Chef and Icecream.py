# Project name : CodeChef: CHFICRM - Chef and Icecream
# Link         : https://www.codechef.com/JUNE20B/problems/CHFICRM
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-06-05
# Description  :
# Status       : Accepted (33714517)
# Tags         : python
# Comment      : 100

from sys import stdin, stdout

no_of_test_cases = int(stdin.readline())

for _ in range(no_of_test_cases):
    no_of_people = int(stdin.readline())
    coins = stdin.readline().strip().split()

    pocket_5 = 0
    pocket_10 = 0

    for coin in coins:
        if coin == '5':
            pocket_5 += 1
        elif coin == '10':
            if pocket_5 > 0:
                pocket_5 -= 1
                pocket_10 += 1
            else:
                stdout.write("NO\n")
                break
        else:
            if pocket_10 > 0:
                pocket_10 -= 1
            elif pocket_5 > 1:
                pocket_5 -= 2
            else:
                stdout.write("NO\n")
                break
    else:
        stdout.write("YES\n")
        
 
