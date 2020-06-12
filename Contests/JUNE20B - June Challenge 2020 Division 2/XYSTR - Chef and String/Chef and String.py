# Project name : CodeChef: XYSTR - Chef and String
# Link         : https://www.codechef.com/JUNE20B/problems/XYSTR
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-06-05
# Description  :
# Status       : Accepted (33710676)
# Tags         : python
# Comment      : 100

from sys import stdin, stdout

no_of_test_cases = int(stdin.readline())

for _ in range(no_of_test_cases):
    S = stdin.readline()
    last_sex = S[0]
    last_0 = 0  # last person is not in a pair
    last_1 = 0  # last person is in a pair
    for sex in S[1:].strip():
        if sex != last_sex:
            last_0, last_1 = max(last_0, last_1), max(last_0 + 1, last_1)

            last_sex = sex
        else:
            last_0 = max(last_0, last_1)
            last_1 = 0

    max_no_of_pairs = max(last_0, last_1)

    stdout.write(str(max_no_of_pairs) + "\n")
