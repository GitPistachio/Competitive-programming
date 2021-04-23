/*
* Project name : HackerRank: Print Prime Numbers
* Link         : https://www.hackerrank.com/challenges/print-prime-numbers/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-23
* Description  :
* Status       : Accepted (210144624)
* Tags         : sql, prime numbers
* Comment      : 
*/

with ODD_NUMBERS_ as
(
    select 2*level + 1 n
    from dual
    connect by level < 500
), PRIME_NUMBERS_ as
(
    select 2 prime
    from DUAL
        union all
    select *
    from ODD_NUMBERS_ od
    where not exists (select * from ODD_NUMBERS_ d where MOD(od.n, d.n) = 0 and od.n <> d.n)
)
select LISTAGG(prime, '&') WITHIN GROUP (order by prime) 
from PRIME_NUMBERS_
;