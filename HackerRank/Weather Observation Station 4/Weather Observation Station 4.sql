/*
* Project name : HackerRank: Weather Observation Station 4
* Link         : https://www.hackerrank.com/challenges/weather-observation-station-4/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-19
* Description  :
* Status       : Accepted (209551885)
* Tags         : sql
* Comment      : 
*/

select count(*) - count(distinct CITY)
from STATION;