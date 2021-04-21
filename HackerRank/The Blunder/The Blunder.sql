/*
* Project name : HackerRank: The Blunder
* Link         : https://www.hackerrank.com/challenges/the-blunder/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-20
* Description  :
* Status       : Accepted (209732353)
* Tags         : sql
* Comment      : 
*/

select 
    ceil(avg(salary) - avg(replace(salary, '0', '')))
from employees;