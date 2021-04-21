/*
* Project name : HackerRank: Revising Aggregations - The Sum Function
* Link         : https://www.hackerrank.com/challenges/revising-aggregations-sum/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-20
* Description  :
* Status       : Accepted (209731179)
* Tags         : sql
* Comment      : 
*/

select sum(population)
from city
where district = 'California';