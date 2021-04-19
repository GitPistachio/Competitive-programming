/*
* Project name : HackerRank: Weather Observation Station 3
* Link         : https://www.hackerrank.com/challenges/weather-observation-station-3/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-19
* Description  :
* Status       : Accepted (209551604)
* Tags         : sql
* Comment      : 
*/

select distinct
    CITY
from STATION
where MOD(ID, 2) = 0;