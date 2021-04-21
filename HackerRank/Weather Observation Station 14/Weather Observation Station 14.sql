/*
* Project name : HackerRank: Weather Observation Station 14
* Link         : https://www.hackerrank.com/challenges/weather-observation-station-14/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-21
* Description  :
* Status       : Accepted (209832749)
* Tags         : sql
* Comment      : 
*/

select cast(max(lat_n) as decimal(20, 4))
from station
where lat_n < 137.2345;