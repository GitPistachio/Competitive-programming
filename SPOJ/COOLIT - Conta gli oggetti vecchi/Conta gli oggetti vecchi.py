# Project name : SPOJ: COOLIT - Conta gli oggetti vecchi
# Author       : Wojciech Raszka
# Date created : 2019-03-27
# Description  :
# Status       : Accepted (23506389)
# Tags         : python
# Comment      :

def countExpiredProducts(x, y):
    if isinstance(x, dict):
        if x['valid'] < 2018 and y['valid'] < 2018:
            return 2
        elif x['valid'] < 2018 or y['valid'] < 2018:
            return 1
        else:
             return 0
    else:
        if y['valid'] < 2018:
            return x + 1
        else:
            return x

from functools import reduce

prod = eval(input())

if len(prod) > 1:
    print(reduce(countExpiredProducts, prod))
elif len(prod) == 1:
    print(countExpiredProducts(0, prod[0]))
else:
    print(0)
