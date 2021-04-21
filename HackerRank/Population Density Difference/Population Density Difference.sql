/*
* Project name : HackerRank: Population Density Difference
* Link         : https://www.hackerrank.com/challenges/population-density-difference/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-20
* Description  :
* Status       : Accepted (209731850)
* Tags         : sql
* Comment      : 
*/

select max(population) - min(population)
from city;