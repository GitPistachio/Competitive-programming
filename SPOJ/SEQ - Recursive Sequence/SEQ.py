# Project name : SPOJ: SEQ - Recursive Sequence
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-03-30
# Description  :
# Status       : Accepted (27627266)
# Tags         : python, math, matrix, modular dot product, fast modular matrix exponentiation, modular matrix multiplication, modular arithmetic
# Comment      : a_n = dot product of first row of M^(n - k) and reversed B. M = [[c1, c2, ..., ck], [1, 0, ..., 0], [0, 1, ..., 0], ..., [0, 0, ..., 0, 1]]

from sys import stdin, stdout

def modularDotProduct(v, w, n, p):
    val = 0
    for i in range(n):
        val += (v[i]*w[i]) % p
     
    return val % p
 
def modularMatrixMultiplication(M, M_shape, N, N_shape, p):
    R = [[0 for _ in range(N_shape[1])] for _ in range(M_shape[0])]
    for i in range(M_shape[0]):
        for j in range(N_shape[1]):
            val = 0
            for k in range(M_shape[1]):
                val += (M[i][k]*N[k][j]) % p
            R[i][j] = val % p
    
    return R
    
def fastModularMatrixExponentiation(M, shape, n, p):
    if n == 1:
        return M
    
    R = fastModularMatrixExponentiation(M, shape, n//2, p)
    if ((n & 1) == 0):
        return modularMatrixMultiplication(R, shape, R, shape, p)
    else:
        return modularMatrixMultiplication(M, shape, modularMatrixMultiplication(R, shape, R, shape, p), shape, p)
 
no_of_tests = int(stdin.readline())
 
p = 1000000000
for _ in range(no_of_tests):
    k = int(stdin.readline())
    B = list(map(int, stdin.readline().split()))
    C = list(map(int, stdin.readline().split()))
    n = int(stdin.readline())
    
    if n <= k:
        a_n = B[n - 1] % p
    else:
        M = [C] # [C.copy()] 
        for i in range(k - 1):
            M.append([1 if i == j else 0 for j in range(k)])
        
        M = fastModularMatrixExponentiation(M, (k, k), n - k, p)
        
        a_n = modularDotProduct(M[0], B[::-1], k, p)
    
    stdout.write('{}\n'.format(a_n))
        