# Project name : CodeChef: SAVKONO - Save Konoha
# Link         : https://www.codechef.com/LRNDSA03/problems/SAVKONO
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-19
# Description  :
# Status       : Accepted (35847738)
# Tags         : python
# Comment      :

from sys import stdin, stdout


MAX_SOLDIER_STRENGTH = 10000

no_of_test_cases = int(stdin.readline())

for _ in range(no_of_test_cases):
    no_of_soldiers, pain_strength = map(int, stdin.readline().split())
    soldiers = [0]*(MAX_SOLDIER_STRENGTH + 1) # create frequency table of soldiers strengths
    for strength in map(int, stdin.readline().split()):
        soldiers[strength] += 1
    
    min_no_of_attacks = 0
    for strength in range(MAX_SOLDIER_STRENGTH, 0, -1):
        if soldiers[strength] > 0:
            x = -(-pain_strength//strength)  # min number of soldiers of given strength necessary to defead the Pain
            no_of_attacks = min(x, soldiers[strength])
            min_no_of_attacks += no_of_attacks
            pain_strength -= no_of_attacks*strength
            if pain_strength <= 0:
                break
            
            half_strength = strength >> 1
            soldiers[half_strength] += no_of_attacks
    
    if pain_strength > 0:
        stdout.write('Evacuate\n')
    else:
        stdout.write(str(min_no_of_attacks) +'\n')
