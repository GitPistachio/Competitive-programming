# Project name : SPOJ: MESSAGEC - Message Relay
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-04-01
# Description  :
# Status       : Accepted (23544204)
# Tags         : python,  graph theory, cycles
# Comment      : 100 points in pypy

def setTypeOfTransmission(i, type_of_transmission, F):
    if F[i] == 0:
        type_of_transmission[i] = 1
        return 1
    else:
        if type_of_transmission[i] is None:
            type_of_transmission[i] = 0
            type_of_transmission[i] = setTypeOfTransmission(F[i] - 1, type_of_transmission, F)
            return type_of_transmission[i]
        elif type_of_transmission[i] == 0:
            return 0
        elif type_of_transmission[i] == 1:
            return 1

N = int(raw_input())

F = [int(raw_input()) for i in range(N)]

type_of_transmission = [None]*N

for i in range(N):
    if type_of_transmission[i] is None:
        setTypeOfTransmission(i, type_of_transmission, F)

no_of_good_transmission = sum(type_of_transmission)
print no_of_good_transmission
