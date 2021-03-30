# Project name : SPOJ: MPOW - Power of matrix
# Link         : https://www.spoj.com/problems/MPOW/
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2020-05-19
# Description  :
# Status       : Accepted (26005698)
# Tags         : python, math, modular arithmetic, matrix, fast modular matrix exponentiation, modular matrix multiplication
# Comment      : 

from sys import stdin, stdout

def matrixMultiplicationModulo(M, M_shape, N, N_shape, p):
    R = [[0 for _ in range(N_shape[1])] for _ in range(M_shape[0])]
    for i in range(M_shape[0]):
        for j in range(N_shape[1]):
            val = 0
            for k in range(M_shape[1]):
                val += (M[i][k]*N[k][j]) % p
            R[i][j] = val % p
    
    return R

def matrixPowerModulo(M, shape, n, p):
    if n == 1:
        return M
    
    R = matrixPowerModulo(M, shape, n//2, p)
    if ((n & 1) == 0):
        return matrixMultiplicationModulo(R, shape, R, shape, p)
    else:
        return matrixMultiplicationModulo(M, shape, matrixMultiplicationModulo(R, shape, R, shape, p), shape, p)

if __name__ == '__main__':
    no_of_tests = int(stdin.readline())
    for _ in range(no_of_tests):
        rows, n = map(int, stdin.readline().split())
        M = []
        for _ in range(rows):
            M.append([int(x) for x in stdin.readline().split()])

        R = matrixPowerModulo(M, (rows, rows), n, 1000000007)
        
        for i in range(rows):
            stdout.write(' '.join(map(str, R[i])) + '\n')