/*
* Project name : HackerRank: Revising Aggregations - The Count Function
* Link         : https://www.hackerrank.com/challenges/revising-aggregations-the-count-function/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-20
* Description  :
* Status       : Accepted (209731009)
* Tags         : sql
* Comment      : 
*/

select count(*)
from city
where population > 100000;