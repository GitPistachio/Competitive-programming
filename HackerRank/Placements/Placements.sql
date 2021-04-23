/*
* Project name : HackerRank: Placements
* Link         : https://www.hackerrank.com/challenges/placements/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-23
* Description  :
* Status       : Accepted (210142067)
* Tags         : sql
* Comment      : 
*/

select s.name 
from Students s
    inner join Friends f on f.ID = s.ID
    inner join Packages sp on sp.ID = s.ID
    inner join Packages fp on fp.ID = f.FRIEND_ID
where fp.SALARY > sp.SALARY
order by fp.SALARY;