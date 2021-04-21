/*
* Project name : HackerRank: Revising Aggregations - Averages
* Link         : https://www.hackerrank.com/challenges/revising-aggregations-the-average-function/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-20
* Description  :
* Status       : Accepted (209731322)
* Tags         : sql
* Comment      : 
*/

select avg(population)
from city
where district = 'California';