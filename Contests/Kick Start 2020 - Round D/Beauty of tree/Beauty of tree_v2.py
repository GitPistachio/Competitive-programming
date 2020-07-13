from sys import stdin, stdout
from collections import defaultdict, deque


no_of_test_cases = int(stdin.readline())

for t in range(1, no_of_test_cases + 1):
    n, a, b = map(int, stdin.readline().split())
    A = [a, b]

    tree = list(map(int, stdin.readline().split()))
    parent = [[0, 0, 0] for _ in range(n)]
    depth = [0]*n
    for i in range(1, n):
        parent[i][0] = tree[i - 1] - 1
        depth[i] = depth[parent[i][0]] + 1

        j = 0
        while parent[i][j]:
            parent[i][j + 1] = parent[parent[i][j]][j]
            j += 1

    cnt = [[0, 0] for _ in range(n)]
    ans = 0
    for i in range(n - 1, -1, -1):
        for j in range(2):
            cnt[i][j] += 1
            if depth[i] < A[j]:
                continue

            cur = i
            k, v = 0, A[j]
            while v:
                if v & 1:
                    cur = parent[cur][k]
                v >>= 1
                k += 1
            print(i, cur, A[j])
            cnt[cur][j] += cnt[i][j]
        va = cnt[i][0]/n
        vb = cnt[i][1]/n
        ans += va + vb - va*vb

    print('Case #{}: {:6f}'.format(t, ans))
