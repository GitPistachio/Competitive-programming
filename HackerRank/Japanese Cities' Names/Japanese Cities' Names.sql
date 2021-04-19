/*
* Project name : HackerRank: Japanese Cities' Names
* Link         : https://www.hackerrank.com/challenges/japanese-cities-name/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-19
* Description  :
* Status       : Accepted (209550546)
* Tags         : sql
* Comment      : 
*/

select name
from CITY
where countrycode = 'JPN';