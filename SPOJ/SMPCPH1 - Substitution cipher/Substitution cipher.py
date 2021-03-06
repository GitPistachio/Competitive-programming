# Project name : SPOJ: SMPCPH1 - Substitution cipher
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-02-24
# Description  :
# Status       : Accepted (23290652)
# Tags         : python, cryptography, substitution cipher
# Comment      :

n = int(input())
#preparing substitution aplhabet
cypher = input()[::-1]
cypher_key = []
for i in range(n):
    cypher_key.append([cypher[i], cypher[i - 1]])

cypher_key[-1][0] = "|"
m = int(input())

for i in range(m):
    s = input().replace(cypher_key[0][1], "|")
    for key, val in cypher_key:
        s = s.replace(key, val)
    print(s)
