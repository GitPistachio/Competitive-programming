no_of_cases = int(input())

for c in range(no_of_cases):
    print(int(str(sum(map(lambda s: int(s[::-1]), input().split(' '))))[::-1]))
