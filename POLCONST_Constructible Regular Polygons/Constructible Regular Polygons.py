# Project name : SPOJ: POLCONST - Constructible Regular Polygons
# Author       : Wojciech Raszka
# Date created : 2019-02-16
# Description  :
# Status       : Accepted (23245541)
# Comment      : n-side polygon is Constructible if n = 2^k*p1*p2*p3... k >= 0 and pi - Fermat prime number


constructible_odd_polygons = set([3,5,17,257,65537,15,51,771,196611,85,1285,327685,4369,1114129,16843009,255,3855,983055,13107,3342387,50529027,21845,5570645,84215045,286331153,65535,16711935,252645135,858993459,1431655765,7158278825])

def isPolygonConstructible(n):
    if n % 2 == 0:
        if n > 4:
            return isPolygonConstructible(n/2)
        elif n == 4:
            return True
    elif n in constructible_odd_polygons:
        return True

    return False


T = int(input())

for t in range(T):
    n = int(input())
    if isPolygonConstructible(n):
        print('Yes')
    else:
        print('No')
