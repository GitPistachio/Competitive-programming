# Project name : HackerRank: Collections.OrderedDict()
# Link         : https://www.hackerrank.com/challenges/py-collections-ordereddict/problem
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.com
# Date created : 2021-04-19
# Description  :
# Status       : Accepted (209533950)
# Tags         : python
# Comment      : 

from collections import OrderedDict

no_of_items = int(input())

bought_items = OrderedDict()
for _ in range(no_of_items):
    item_name, price = input().rstrip().rsplit(' ', 1)
    bought_items[item_name] = bought_items.get(item_name, 0) + int(price)
    
for item_name, net_price in bought_items.items():
    print(item_name, net_price)
