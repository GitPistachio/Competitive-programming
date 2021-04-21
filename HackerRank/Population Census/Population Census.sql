/*
* Project name : HackerRank: Population Census
* Link         : https://www.hackerrank.com/challenges/asian-population/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-20
* Description  :
* Status       : Accepted (209730736)
* Tags         : sql
* Comment      : 
*/

select sum(ct.population)
from city ct
    inner join country cn on cn.code = ct.countrycode
where cn.continent = 'Asia';