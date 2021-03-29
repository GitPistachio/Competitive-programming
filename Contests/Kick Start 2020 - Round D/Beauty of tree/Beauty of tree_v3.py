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

setrecursionlimit(1000000)

def dfs(vid, depth):
    global counts_a
    global counts_b
    global a
    global b
    global ans
    count_a = counts_a[depth % a]
    count_b = counts_b[depth % b]

    counts_a[depth % a] += 1
    counts_b[depth % b] += 1
    for vnid in adjacency_list[vid]:
        dfs(vnid, depth + 1)

    pa = (counts_a[depth % a] - count_a)/n
    pb = (counts_b[depth % b] - count_b)/n

    ans += pa + pb - pa*pb


no_of_test_cases = int(stdin.readline())

for t in range(1, no_of_test_cases + 1):
    n, a, b = map(int, stdin.readline().split())

    tree = list(map(int, stdin.readline().split()))
    adjacency_list = [[] for _ in range(n)]
    for i in range(n - 1):
        adjacency_list[tree[i] - 1].append(i + 1)

    counts_a = [0]*n
    counts_b = [0]*n
    ans = 0.0

    dfs(0, 0)

    print('Case #{}: {:6f}'.format(t, ans))
