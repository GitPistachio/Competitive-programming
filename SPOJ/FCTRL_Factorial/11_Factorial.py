def Z(n):
    d = 5
    no_of_zeros = 0
    while d <= n:
        no_of_zeros += n//d
        d *= 5

    return no_of_zeros

T = int(input())
N = [int(input()) for i in range(T)]

for n in N:
    print(Z(n))
