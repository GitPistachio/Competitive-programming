/*
* Project name : HackerRank: Weather Observation Station 19
* Link         : https://www.hackerrank.com/challenges/weather-observation-station-19/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-21
* Description  :
* Status       : Accepted (209838956)
* Tags         : sql, euclidean distance
* Comment      : 
*/

select round(sqrt(power(min(lat_n) - max(lat_n), 2) + power(min(long_w) - max(long_w), 2)), 4)
from station;