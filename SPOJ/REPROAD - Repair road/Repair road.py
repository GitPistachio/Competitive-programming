# Project name : SPOJ: REPROAD - Repair road
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2019-04-27
# Description  :
# Status       : Accepted (23689995)
# Tags         : python, sliding window technique
# Comment      :

def maxNoOfConsecutiveBlocks(R, m, k):
    max_no_of_consecutive_blocks = 0

    no_of_consecutive_blocks = 0
    starting_block = 0
    for i in range(m):
        if R[i] == '1':
            no_of_consecutive_blocks += 1
        elif k > 0:
            no_of_consecutive_blocks += 1
            k -= 1
        else:
            max_no_of_consecutive_blocks = max(max_no_of_consecutive_blocks, no_of_consecutive_blocks)
            while starting_block < m:
                if R[starting_block] == '0':
                    starting_block += 1
                    break
                else:
                    no_of_consecutive_blocks -= 1
                starting_block += 1

    return max(max_no_of_consecutive_blocks, no_of_consecutive_blocks)

T = int(input())

while T > 0:
    m, k = map(int, input().split())
    R = input().split()

    print(maxNoOfConsecutiveBlocks(R, m, k))
    T -= 1
