/*
* Project name : HackerRank: Weather Observation Station 11
* Link         : https://www.hackerrank.com/challenges/weather-observation-station-11/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-19
* Description  :
* Status       : Accepted (209567290)
* Tags         : sql
* Comment      : 
*/

select distinct
    city
from STATION
where lower(substr(city, 1, 1)) not in ('a', 'e', 'i', 'o', 'u')
    or lower(substr(city, length(city), 1)) not in ('a', 'e', 'i', 'o', 'u');