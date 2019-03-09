# Project name : SPOJ: SUMGCD - Sum of GCD
# Author       : Wojciech Raszka
# Date created : 2019-02-24
# Description  :
# Status       :
# Comment      :

MAX = 1000001

phi = [0]*MAX
result = [0]*MAX

def precomputeTotient():
    phi[1] = 1
    for i in range(2, MAX):
        if not phi[i]:
            for j in range(i << 1, MAX, i):
                if not phi[j]:
                    phi[j] = j
                phi[j] = (phi[j]//i)*(i - 1)

def precomputeSumOfGCDPairs():
    precomputeTotient()

    for  i in range(MAX):
        for j in range(2, MAX):
            if i*j >= MAX:
                break
            result[i * j] += i * phi[j]

    for i in range(2, MAX):
        result[i] += result[i - 1]

precomputeSumOfGCDPairs()
