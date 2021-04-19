/*
* Project name : HackerRank: Revising the Select Query II
* Link         : https://www.hackerrank.com/challenges/revising-the-select-query-2/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-19
* Description  :
* Status       : Accepted (209550105)
* Tags         : sql
* Comment      : 
*/

select NAME
from CITY
where countrycode = 'USA'
    and population > 120000;