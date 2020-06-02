# Project name : CodeChef: LADDU - Laddu
# Link         : https://www.codechef.com/LRNDSA01/problems/LADDU
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio
# Date created : 2020-06-02
# Description  :
# Status       : Accepted (33570487)
# Tags         : python
# Comment      :

from sys import stdin, stdout

no_of_test_cases = int(stdin.readline())


for _ in range(no_of_test_cases):
    no_of_activities, origin = stdin.readline().split()
    no_of_activities = int(no_of_activities)
    collected_laddus = 0
    for _ in range(no_of_activities):
        activity = stdin.readline().split()
        if activity[0] == "CONTEST_WON":
            collected_laddus += 300 + max(0, 20 - int(activity[1]))
        elif activity[0] == "TOP_CONTRIBUTOR":
            collected_laddus += 300
        elif activity[0] == "BUG_FOUND":
            collected_laddus += int(activity[1])
        else:
            collected_laddus += 50
        
    if origin == "INDIAN":
        max_no_of_month = collected_laddus//200
    else:
        max_no_of_month = collected_laddus//400
        
    stdout.write(str(max_no_of_month) + "\n")
