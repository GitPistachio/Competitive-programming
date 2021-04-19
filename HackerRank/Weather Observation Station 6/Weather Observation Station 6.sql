/*
* Project name : HackerRank: Weather Observation Station 6
* Link         : https://www.hackerrank.com/challenges/weather-observation-station-6/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-19
* Description  :
* Status       : Accepted (209565912)
* Tags         : sql
* Comment      : 
*/

select distinct
    city
from STATION
where lower(substr(city, 1, 1)) in ('a', 'e', 'i', 'o', 'u');