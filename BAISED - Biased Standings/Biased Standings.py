# Project name : SPOJ: BAISED - Biased Standings
# Author       : Wojciech Raszka
# Date created : 2019-03-17
# Description  :
# Status       : Accepted (23432596)
# Comment      : O(n)

T = int(raw_input())

while (T > 0):
  raw_input()
  N = int(raw_input())
  prefered_position = [0]*(N + 1)
  for i in range(N):
    team, rank = raw_input().split()
    prefered_position[int(rank)] += 1

  badness = 0
  position = 1
  for i in range(1, N + 1):
    if i <= position:
        badness += (prefered_position[i] - 1)*prefered_position[i]/2 + prefered_position[i]*(position - i)
    elif position + prefered_position[i] - 1 <= i:
        badness += (prefered_position[i] - 1)*prefered_position[i]/2 + prefered_position[i]*(i - position - prefered_position[i] + 1)
    else:
        badness += (i - position)*(i - position + 1)/2 + (position + prefered_position[i] - i - 1)*(position + prefered_position[i] - i)/2

    position += prefered_position[i]

  print badness

  T -= 1
