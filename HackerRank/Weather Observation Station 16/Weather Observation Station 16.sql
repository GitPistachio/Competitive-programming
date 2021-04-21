/*
* Project name : HackerRank: Weather Observation Station 16
* Link         : https://www.hackerrank.com/challenges/weather-observation-station-16/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-21
* Description  :
* Status       : Accepted (209833520)
* Tags         : sql
* Comment      : 
*/

select round(min(lat_n), 4)
from station
where lat_n > 38.7780;