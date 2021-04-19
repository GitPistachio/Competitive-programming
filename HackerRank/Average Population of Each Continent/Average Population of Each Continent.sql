/*
* Project name : HackerRank: Average Population of Each Continent
* Link         : https://www.hackerrank.com/challenges/average-population-of-each-continent/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-19
* Description  :
* Status       : Accepted (209569247)
* Tags         : sql
* Comment      : 
*/

select
    cn.continent
  , floor(avg(ct.population)) avg_city_population
from city ct
    inner join country cn on cn.code = ct.countrycode
group by cn.continent;