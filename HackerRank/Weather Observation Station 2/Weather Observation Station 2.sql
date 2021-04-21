/*
* Project name : HackerRank: Weather Observation Station 2
* Link         : https://www.hackerrank.com/challenges/weather-observation-station-2/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-21
* Description  :
* Status       : Accepted (209831981)
* Tags         : sql
* Comment      : 
*/

select round(sum(lat_n), 2), round(sum(long_w), 2)
from station;