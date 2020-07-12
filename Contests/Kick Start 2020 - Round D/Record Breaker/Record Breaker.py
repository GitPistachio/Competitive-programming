from sys import stdin, stdout

no_of_test_cases = int(stdin.readline())

for t in range(1, no_of_test_cases + 1):
    n = int(stdin.readline())
    V = list(map(int, stdin.readline().split()))

    moving_max_v = -1
    no_of_record_breakrs = 0
    for i in range(n):
        if V[i] > moving_max_v:
            moving_max_v = V[i]

            if i == n - 1 or V[i] > V[i + 1]:
                no_of_record_breakrs += 1

    stdout.write('Case #' + str(t) + ': ' + str(no_of_record_breakrs) + '\n')
