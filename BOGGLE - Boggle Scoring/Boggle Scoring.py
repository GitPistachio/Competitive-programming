# Project name : SPOJ: BOGGLE - Boggle Scoring
# Author       : Wojciech Raszka
# Date created : 2019-03-18
# Description  :
# Status       : Accepted (23450293)
# Comment      :


def score(no_of_letters):
    if no_of_letters <= 4:
        return 1
    elif no_of_letters == 5:
        return 2
    elif no_of_letters == 6:
        return 3
    elif no_of_letters == 7:
        return 5
    else:
        return 11

no_of_players = int(input())

words = []
for player in range(no_of_players):
    words.append(set(input().split()))

max_score = 0
for p_i in range(no_of_players):
    p_i_words = words[p_i]
    for p_j in range(no_of_players):
        if p_i != p_j:
            p_i_words = p_i_words.difference(words[p_j])

    p_i_score = sum(map(lambda x: score(len(x)), p_i_words))
    if p_i_score > max_score:
        max_score = p_i_score

print(max_score)
