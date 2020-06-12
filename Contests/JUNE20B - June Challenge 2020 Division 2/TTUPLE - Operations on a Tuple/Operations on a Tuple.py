# Project name : CodeChef: TTUPLE - Operations on a Tuple
# Link         : https://www.codechef.com/JUNE20B/problems/TTUPLE
# Try it on    : 
# Author       : Wojciech Raszka
# E-mail       : contact@gitpistachio.site
# Date created : 2020-06-06
# Description  :
# Status       : Accepted (33732001)
# Tags         : python
# Comment      : 100

from sys import stdin, stdout
from itertools import permutations


def solve2d(p, q, a, b):
    """Solve for 2 when p != a and q != b."""
    if a - p == b - q or (p != 0 and q != 0 and a % p == 0 and b % q == 0 and a*q == b*p):
        return 1

    return 2


def solve3opt22aa(p, q, r, a, b, c):
    if a - p + q - b + c - r == 0:
        return 2

    return 3


def solve3opt22am(p, q, r, a, b, c):
    if r != 0 and c % r == 0 and (q + a - p)*c == b*r:
        return 2

    return 3


def solve3opt22mm(p, q, r, a, b, c):
    if p != 0 and q != 0 and r != 0 and a % p == 0 and b % q == 0 and c % r == 0 and q*a*c == b*p*r:
        return 2

    return 3


def solve3opt22ma(p, q, r, a, b, c):
    if p != 0 and a % p == 0 and q*a + p*(c - r) == b*p:
        return 2

    return 3


def solve3opt32am(p, q, r, a, b, c):
    u = a - p
    if q + u == 0 and r + u == 0:
        return 3

    if q + u != 0:
        v = b//(q + u)
    else:
        v = c//(r + u)

    if v*(q + u) == b and v*(r + u) == c:
        return 2

    return 3


def solve3opt32ma(p, q, r, a, b, c):
    if p == 0:
        return 3

    u = a//p
    if u*p != a:
        return 3

    v = b - q*u
    if r*u + v == c:
        return 2

    return 3


def solve3opt23ma(p, q, r, a, b, c):
    v = c - r
    if v == 0:
        return 3

    if p == 0 and q == 0:
        return 3

    if p != 0:
        u = (a - v)//p
    else:
        u = (b - v)//q

    if u*p == a - v and u*q == b - v:
        return 2

    return 3


def solve3opt33ma(p, q, r, a, b, c):
    if r == p:
        return 3

    v = (c - a)//(r - p)

    if v*(r - p) != (c - a):
        return 3

    if a + (q - p)*v == b:
        return 2

    return 3


def solve3opt33am(p, q, r, a, b, c):
    if a == b:
        return 3

    u = (p*b - a*q)//(a - b)

    if u*(a - b) != (p*b - a*q):
        return 3

    if q + u == 0 and p + u == 0:
        return 3

    if q + u != 0:
        v = b//(q + u)
        if v*(q + u) != b:
            return 3
    else:
        v = a//(p + u)
        if v*(p + u) != a:
            return 3

    if (r + u)*v == c:
        return 2

    return 3


def solve31(p, q, r, a, b, c):
    # tuples are the same, nothing to do
    if p == a and q == b and r == c:
        return 0

    # tuples differ with only one element, thus single operation is enough
    if ((p == a and q == b and r != c)
       or (p == a and q != b and r == c)
       or (p != a and q == b and r == c)):
        return 1

    # tuples differ on two elements
    if p == a or q == b or r == c:
        if p == a:
            return solve2d(q, r, b, c)
        elif q == b:
            return solve2d(p, r, a, c)
        else:
            return solve2d(p, q, a, b)

    # tuples differ on three elements

    if (a - p == b - q == c - r) or (p != 0 and q != 0 and r != 0 and a % p == 0 and b % q == 0 and c % r == 0 and a*q == b*p and b*r == c*q and a*r == c*p):
        return 1

    opt12 = 1 + min(solve2d(p, q, a, b), solve2d(p, r, a, c), solve2d(q, r, b, c))
    opt22 = 3
    opt32 = 3
    opt23 = 3
    opt33 = 3
    min_opt = opt12
    for t1, t2 in zip(permutations([p, q, r]), permutations([a, b, c])):
        opt22 = min(solve3opt22aa(*t1, *t2),
                    solve3opt22am(*t1, *t2),
                    solve3opt22mm(*t1, *t2),
                    solve3opt22ma(*t1, *t2),
                    opt22)

        opt32 = min(solve3opt32am(*t1, *t2),
                    solve3opt32ma(*t1, *t2),
                    opt32)

        opt23 = min(solve3opt23ma(*t1, *t2),
                    opt23)

        opt33 = min(solve3opt33am(*t1, *t2),
                    solve3opt33ma(*t1, *t2),
                    opt33)

        min_opt = min(min_opt, opt22, opt32, opt23, opt33)
        if min_opt == 2:
            break

    return min_opt


no_of_test_cases = int(stdin.readline())
for _ in range(no_of_test_cases):
    t1 = [int(x) for x in stdin.readline().split()]
    t2 = [int(x) for x in stdin.readline().split()]

    no_of_operations = solve31(*t1, *t2)
    stdout.write(str(no_of_operations) + "\n")
