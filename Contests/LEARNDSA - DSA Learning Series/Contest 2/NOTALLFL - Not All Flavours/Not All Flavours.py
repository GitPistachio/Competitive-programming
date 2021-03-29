# Project name : CodeChef: NOTALLFL - Not All Flavours
# Link         : https://www.codechef.com/LRNDSA02/problems/NOTALLFL
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-06-19
# Description  :
# Status       : Accepted (34522326)
# Tags         : python, linear data structure, sliding window technique, stack
# Comment      :


from sys import exit, stdin, stdout


MAX_NO_OF_FLAVOURS = 100000


no_of_test_cases = int(stdin.readline())
for _ in range(no_of_test_cases):
    no_of_cakes, no_of_flavours = map(int, stdin.readline().split())
    cakes_flavours = [int(x) for x in stdin.readline().split()]
    
    flavours = [0]*no_of_flavours
    no_of_missing_flavours = no_of_flavours
    tail_position = 0
    result = 0
    for i in range(no_of_cakes):
        flavour = cakes_flavours[i] - 1
        if flavours[flavour] == 0:
            no_of_missing_flavours -= 1
        
        flavours[flavour] += 1
        
        if no_of_missing_flavours == 0:
            while tail_position <= i:
                former_flavour = cakes_flavours[tail_position] - 1
                flavours[former_flavour] -= 1
                tail_position += 1
                if flavours[former_flavour] == 0:
                    no_of_missing_flavours += 1
                    break
        
        if result < i - tail_position + 1:
            result = i - tail_position + 1

    
    stdout.write(str(result) +'\n')
