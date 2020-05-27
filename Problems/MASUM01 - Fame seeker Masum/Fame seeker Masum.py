# Project name : SPOJ: MASUM01 - Fame seeker Masum
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-11-12
# Description  :
# Status       : Accepted (24842653)
# Tags         : python, string pattern
# Comment      :

from sys import stdin, stdout

word = 'masum'

i = 0
j = 0
rejected_idx = []
for letter in stdin.readline().strip():
  if j >= len(word) or letter != word[j]:
    rejected_idx.append(str(i + 1))
  else:
    j += 1

  i += 1


if len(rejected_idx) == 0:
  stdout.write('Nothing to delete')
else:
  stdout.write(' '.join(rejected_idx))
