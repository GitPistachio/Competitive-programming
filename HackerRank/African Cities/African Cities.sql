/*
* Project name : HackerRank: African Cities
* Link         : https://www.hackerrank.com/challenges/african-cities/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-19
* Description  :
* Status       : Accepted (209568607)
* Tags         : sql
* Comment      : 
*/

select 
    ct.name
from CITY ct
    inner join COUNTRY cn on cn.code = ct.countrycode
where cn.continent = 'Africa';