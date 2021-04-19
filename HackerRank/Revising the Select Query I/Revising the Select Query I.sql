/*
* Project name : HackerRank: Revising the Select Query I
* Link         : https://www.hackerrank.com/challenges/revising-the-select-query/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-19
* Description  :
* Status       : Accepted (209549461)
* Tags         : sql
* Comment      : 
*/

select *
from CITY
where CountryCode = 'USA'
    and Population > 100000;