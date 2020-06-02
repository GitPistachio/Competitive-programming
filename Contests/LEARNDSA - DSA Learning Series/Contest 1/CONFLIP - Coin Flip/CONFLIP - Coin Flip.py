# Project name : CodeChef: CONFLIP - Coin Flip
# Link         : https://www.codechef.com/LRNDSA01/problems/CONFLIP
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio
# Date created : 2020-06-02
# Description  :
# Status       : Accepted (33570566)
# Tags         : python, game theory, coin flip, sequence A004526 (OEIS)
# Comment      :

from sys import stdin, stdout


def solve(starting_coin_state, no_of_coins, demand_state):
    no_of_heads = no_of_coins//2
    no_of_tails = no_of_coins - no_of_heads
    
    if starting_coin_state == 2:
        no_of_heads, no_of_tails = no_of_tails, no_of_heads
    
    if demand_state == 1:
        return no_of_heads
    else:
        return no_of_tails
    

no_of_test_cases = int(stdin.readline())

for _ in range(no_of_test_cases):
    no_of_games = int(stdin.readline())
    for _ in range(no_of_games):
        starting_coin_state, no_of_coins, demand_state = map(int, stdin.readline().split())
        result = solve(starting_coin_state, no_of_coins, demand_state)
        stdout.write(str(result) + "\n")
