# Project name : CodeChef: LAPIN - Lapindromes
# Link         : https://www.codechef.com/LRNDSA01/problems/LAPIN
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio
# Date created : 2020-06-02
# Description  :
# Status       : Accepted (33570321)
# Tags         : python, lapindrome
# Comment      :

from sys import stdin, stdout

def is_lapindrome_en_aplhabet(x):
    n = len(x)
    ord_a = ord('a')
    freq_tab = [0]*(ord('z') - ord_a + 1)
    
    for c in x[:n//2]:
        freq_tab[ord(c) - ord_a] += 1
    
    for c in x[n//2 + (n & 1):]:
        i = ord(c) - ord_a
        if freq_tab[i] <= 0:
            return False
        
        freq_tab[i] -= 1

    if sum(freq_tab) > 0:
        return False
    
    return True


no_of_test_cases = int(stdin.readline())

for _ in range(no_of_test_cases):
    if is_lapindrome_en_aplhabet(stdin.readline().strip()):
        stdout.write("YES\n")
    else:
        stdout.write("NO\n")
