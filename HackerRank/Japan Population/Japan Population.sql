/*
* Project name : HackerRank: Japan Population
* Link         : https://www.hackerrank.com/challenges/japan-population/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-20
* Description  :
* Status       : Accepted (209731629)
* Tags         : sql
* Comment      : 
*/

select sum(population)
from city
where countrycode = 'JPN';