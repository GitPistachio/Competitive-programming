/*
* Project name : HackerRank: Weather Observation Station 5
* Link         : https://www.hackerrank.com/challenges/weather-observation-station-5/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-19
* Description  :
* Status       : Accepted (209565450)
* Tags         : sql
* Comment      : 
*/

select *
from
(
    select
        city, length(city)
    from STATION
    order by 2, 1
) d
where rownum = 1
union all
select *
from
(
    select
        city, length(city)
    from STATION
    order by 2 desc, 1
) d
where rownum = 1;