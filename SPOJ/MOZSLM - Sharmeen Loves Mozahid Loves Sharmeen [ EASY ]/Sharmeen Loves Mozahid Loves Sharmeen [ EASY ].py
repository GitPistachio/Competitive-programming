# Project name : SPOJ: MOZSLM - Sharmeen Loves Mozahid Loves Sharmeen [ EASY ]
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-11-12
# Description  :
# Status       : Accepted (24841862)
# Tags         : python, string pattern, binary search algorithm, find the index of the first larger element than given value in an sorted array
# Comment      :

from sys import stdin, stdout

def findFirstIdxOfLargerElement(A, a, l, r):
  idx = None
  while l <= r:
    mid = l + (r - l)//2
    if A[mid] <= a:
      l = mid + 1
    else:
      idx = mid
      r = mid - 1

  return idx

T = int(stdin.readline())

while T > 0:
  S = []
  M = []
  p = 0
  for l in stdin.readline():
    if l == 's':
      S.append(p)
    elif l == 'm':
      M.append(p)

    p += 1

  s_len = len(S)
  m_len = len(M)

  no_of_com = 0
  last_idx_m = 0
  for i in range(s_len):
    idx_m = findFirstIdxOfLargerElement(M, S[i], last_idx_m, m_len - 1)
    if idx_m is None:
      break

    last_idx_m = idx_m
    for j in range(idx_m, m_len):
      idx_s = findFirstIdxOfLargerElement(S, M[j], i + 1, s_len - 1)
      if idx_s is None:
        break

      no_of_com += s_len - idx_s

  stdout.write('%s\n' % no_of_com)

  T -= 1
