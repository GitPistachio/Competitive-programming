/*
* Project name : HackerRank: Weather Observation Station 9
* Link         : https://www.hackerrank.com/challenges/weather-observation-station-9/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-19
* Description  :
* Status       : Accepted (209566735)
* Tags         : sql
* Comment      : 
*/

select distinct
    city
from STATION
where lower(substr(city, 1, 1)) not in ('a', 'e', 'i', 'o', 'u');