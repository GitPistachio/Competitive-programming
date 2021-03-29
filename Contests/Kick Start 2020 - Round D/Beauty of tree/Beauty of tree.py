# Project name : Google: Kick Start 2020 - Round D: Beauty tree
# Link         : https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000386edd
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 
# Description  :
# Status       : 
# Tags         : python
# Comment      :

from sys import stdin, stdout, setrecursionlimit
from collections import defaultdict


setrecursionlimit(500000)


def dfs(freq, adjacency_list, vid, vid_depth, skip):
    vid_freq_by_depth = defaultdict(int)
    vid_freq_by_depth[vid_depth] += 1
    for vnid in adjacency_list[vid]:
        vnid_freq_by_depth = dfs(freq, adjacency_list, vnid, vid_depth + 1, skip)
        for depth, count in vnid_freq_by_depth.items():
            vid_freq_by_depth[depth] += count

    freq[vid] = 0
    for depth, count in vid_freq_by_depth.items():
        if (depth - vid_depth) % skip == 0:
            freq[vid] += count

    return vid_freq_by_depth


no_of_test_cases = int(stdin.readline())

for t in range(1, no_of_test_cases + 1):
    n, a, b = map(int, stdin.readline().split())

    parent = list(map(int, stdin.readline().split()))
    adjacency_list = [[] for _ in range(n)]
    for i in range(n - 1):
        adjacency_list[parent[i] - 1].append(i + 1)

    freq_a = [0]*n
    freq_b = [0]*n
    dfs(freq_a, adjacency_list, 0, 0, a)
    dfs(freq_b, adjacency_list, 0, 0, b)

    ans = 0.0
    for i in range(n):
        p_a = freq_a[i]/n
        p_b = freq_b[i]/n
        ans += p_a + p_b - p_a*p_b

    print('Case #{}: {:6f}'.format(t, ans))
