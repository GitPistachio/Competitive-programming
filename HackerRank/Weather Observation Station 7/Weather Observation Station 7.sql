/*
* Project name : HackerRank: Weather Observation Station 7
* Link         : https://www.hackerrank.com/challenges/weather-observation-station-7/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-19
* Description  :
* Status       : Accepted (209566382)
* Tags         : sql
* Comment      : 
*/

select distinct
    city
from STATION
where lower(substr(city, length(city), 1)) in ('a', 'e', 'i', 'o', 'u');