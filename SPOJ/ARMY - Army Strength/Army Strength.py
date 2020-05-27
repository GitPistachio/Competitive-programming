# Project name : SPOJ: ARMY - Army Strength
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-11-18
# Description  :
# Status       : Accepted (24893661)
# Tags         : python, game theory
# Comment      :

from sys import stdin, stdout

T = int(stdin.readline())

while T > 0:
  stdin.readline() #read empty line
  ng, nm = map(int, stdin.readline().split())
  godzilla_best_soldier = max(map(int, stdin.readline().split()))
  mechagodzilla_best_soldier = max(map(int, stdin.readline().split()))

  if godzilla_best_soldier >= mechagodzilla_best_soldier:
    stdout.write('Godzilla\n')
  else:
    stdout.write('MechaGodzilla\n')

  T -= 1
