from sys import stdin, stdout

no_of_test_cases = int(stdin.readline())

for t in range(1, no_of_test_cases + 1):
    k = int(stdin.readline().strip())
    A = list(map(int, stdin.readline().strip().split()))

    lv1, lv2, lv3, lv4 = 0, 0, 0, 0

    for i in range(1, k):
        if A[i] > A[i - 1]:
            v1 = min(lv1, lv2, lv3, lv4) + 1
            v2 = min(lv1, min(lv2, lv3, lv4) + 1)
            v3 = min(lv1, lv2, min(lv3, lv4) + 1)
            v4 = min(lv1, lv2, lv3, lv4 + 1)

            lv1, lv2, lv3, lv4 = v1, v2, v3, v4
        elif A[i] < A[i - 1]:
            v4 = min(lv1, lv2, lv3, lv4) + 1
            v3 = min(min(lv1, lv2, lv3) + 1, lv4)
            v2 = min(min(lv1, lv2) + 1, lv3, lv4)
            v1 = min(lv1 + 1, lv2, lv3, lv4)

            lv1, lv2, lv3, lv4 = v1, v2, v3, v4

    no_of_break_rules = min(lv1, lv2, lv3, lv4)

    stdout.write('Case #' + str(t) + ': ' + str(no_of_break_rules) + '\n')
