/*
* Project name : HackerRank: Weather Observation Station 18
* Link         : https://www.hackerrank.com/challenges/weather-observation-station-18/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-21
* Description  :
* Status       : Accepted (209834626)
* Tags         : sql, manhattan distance
* Comment      : 
*/

select round(max(lat_n) - min(lat_n) + max(long_w) - min(long_w), 4)
from station;