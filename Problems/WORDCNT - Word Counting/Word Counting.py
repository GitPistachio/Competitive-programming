# Project name : SPOJ: WORDCNT - Word Counting
# Author       : Wojciech Raszka
# E-mail       : gitpistachio@gmail.com
# Date created : 2019-06-05
# Description  :
# Status       : Accepted (23880477)
# Tags         : python
# Comment      :

from sys import stdin, stdout

T = int(stdin.readline())

while T > 0:
    n = 0
    len_of_con_seq = 1
    max_len_of_con_seq = 1
    tokens = stdin.readline().split()
    if len(tokens) > 0:
        for word in tokens:
            if len(word) == n:
                len_of_con_seq += 1
                if len_of_con_seq > max_len_of_con_seq:
                    max_len_of_con_seq = len_of_con_seq
            else:
                n = len(word)
                len_of_con_seq = 1

        stdout.write("%d\n" % max_len_of_con_seq)

        T -= 1
