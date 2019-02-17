# Project name : SPOJ: Candy III
# Author       : Wojciech Raszka
# Date created : 2019-02-08
# Description  :
# Status       : Accepted (23195938)
# Comment      :
from math import floor, ceil


for a in range(6, 101):
    cube_of_a = a*a*a
    no_of_operations = 0
    for b in range(2, a - 1):
        cube_of_b = b*b*b
        eq = floor((cube_of_a - cube_of_b)**(1/3))
        for c in range(b, eq + 1):
            no_of_operations += 1
            cube_of_c = c*c*c
            cube_of_d = cube_of_a - cube_of_b - cube_of_c
            d = ceil((cube_of_a - cube_of_b - cube_of_c)**(1/3))
            if d*d*d == cube_of_d and d >= c:
                print("Cube = ", a, ", Triple = (", b, ",", c, ",", d, ")", sep='')
