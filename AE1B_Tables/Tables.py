# Project name : SPOJ: Tables
# Author       : Wojciech Raszka
# Date created : 2019-02-06
# Description  :
# Status       : Accepted (23185689)
# Comment      :

n, k, s = list(map(int, input().split(' ')))

A = sorted(map(int, input().split(' ')), reverse=True)

needed_no_of_screws = k*s
cum_no_of_screws = 0

no_of_boxes = 0
for no_of_screws in A:
    cum_no_of_screws += no_of_screws
    no_of_boxes += 1
    if cum_no_of_screws >= needed_no_of_screws:
        print(no_of_boxes)
        break
