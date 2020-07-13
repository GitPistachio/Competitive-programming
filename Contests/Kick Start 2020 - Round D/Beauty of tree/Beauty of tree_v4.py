# Project name : Google: Kick Start 2020 - Round D: Beauty tree
# Link         : https://codingcompetitions.withgoogle.com/kickstart/round/000000000019ff08/0000000000386edd
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-07-13
# Description  :
# Status       : Accepted
# Tags         : python, tree, DFS, depth firsh traversal, iterative depth firsh traversal
# Comment      :

from sys import stdin, stdout


def dfs(vid):
    global adjacency_list
    global n
    global ans

    counts_by_depth_a = [0]*n
    counts_by_v_a = [0]*n
    counts_by_depth_b = [0]*n
    counts_by_v_b = [0]*n
    depth = [0]*n
    visited = [False]*n
    stack = [-1]*n
    stack[0] = vid
    i = 0
    while i >= 0:
        vid = stack[i]
        vid_depth = depth[vid]
        if visited[vid]:
            i -= 1
            pa = (counts_by_depth_a[vid_depth % a] - counts_by_v_a[vid])/n
            pb = (counts_by_depth_b[vid_depth % b] - counts_by_v_b[vid])/n
            ans += pa + pb - pa*pb
        else:
            counts_by_v_a[vid] = counts_by_depth_a[vid_depth % a]
            counts_by_v_b[vid] = counts_by_depth_b[vid_depth % b]
            counts_by_depth_a[vid_depth % a] += 1
            counts_by_depth_b[vid_depth % b] += 1
            visited[vid] = True
            for vnid in adjacency_list[vid]:
                i += 1
                stack[i] = vnid
                depth[vnid] = vid_depth + 1


no_of_test_cases = int(stdin.readline())

for t in range(1, no_of_test_cases + 1):
    n, a, b = map(int, stdin.readline().split())

    tree = list(map(int, stdin.readline().split()))
    adjacency_list = [[] for _ in range(n)]
    for i in range(n - 1):
        adjacency_list[tree[i] - 1].append(i + 1)

    ans = 0.0

    dfs(0)

    print('Case #{}: {:6f}'.format(t, ans))
