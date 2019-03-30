# Project name : SPOJ: ENCAROC - Occurrences of a Character
# Author       : Wojciech Raszka
# Date created : 2019-03-24
# Description  :
# Status       : Accepted (23483741)
# Tags         : python
# Comment      :

sentence = input()
letter = input().strip()

print(len(sentence)- len(sentence.replace(letter, "")))
