/*
* Project name : HackerRank: Weather Observation Station 15
* Link         : https://www.hackerrank.com/challenges/weather-observation-station-15/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-21
* Description  :
* Status       : Accepted (209833244)
* Tags         : sql
* Comment      : 
*/

select round(long_w, 4)
from station
where lat_n = (select max(lat_n) from station where lat_n < 137.2345);