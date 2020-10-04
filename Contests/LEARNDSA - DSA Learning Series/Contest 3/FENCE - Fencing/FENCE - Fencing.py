# Project name : CodeChef: FENCE - Fencing
# Link         : https://www.codechef.com/LRNDSA03/problems/FENCE
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-19
# Description  :
# Status       : Accepted (35847842)
# Tags         : python
# Comment      :

from sys import stdin, stdout


no_of_test_cases = int(stdin.readline())

for _ in range(no_of_test_cases):
    n, m, no_of_plants = map(int, stdin.readline().split())
    
    
    min_req_len_of_fence = 4*no_of_plants  # maximum length of fence, no two plants have common side
    plants = set()
    for _ in range(no_of_plants):
        x, y = map(int, stdin.readline().split())
        plants.add((x, y))
        
        if (x - 1, y) in plants:
            min_req_len_of_fence -= 2
        
        if (x + 1, y) in plants:
            min_req_len_of_fence -= 2
        
        if (x, y - 1) in plants:
            min_req_len_of_fence -= 2
        
        if (x, y + 1) in plants:
            min_req_len_of_fence -= 2
    
    stdout.write(str(min_req_len_of_fence) + '\n')