/*
* Project name : HackerRank: Weather Observation Station 13
* Link         : https://www.hackerrank.com/challenges/weather-observation-station-13/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-21
* Description  :
* Status       : Accepted (209832369)
* Tags         : sql
* Comment      : 
*/

select sum(lat_n)
from station
where lat_n > 38.7880 and lat_n < 137.2345;