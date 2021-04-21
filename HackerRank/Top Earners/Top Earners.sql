/*
* Project name : HackerRank: Top Earners
* Link         : https://www.hackerrank.com/challenges/earnings-of-employees/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-21
* Description  :
* Status       : Accepted (209831467)
* Tags         : sql
* Comment      : 
*/

select *
from
(
select salary*months, count(*) 
from employee
group by salary*months
order by 1 desc
) d
where rownum <= 1;