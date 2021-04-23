/*
* Project name : HackerRank: The Report
* Link         : https://www.hackerrank.com/challenges/the-report/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-22
* Description  :
* Status       : Accepted (209882377)
* Tags         : sql
* Comment      : 
*/

select case when g.grade >= 8 then s.name end, g.grade, s.marks
from students s
    inner join grades g on s.marks between g.min_mark and g.max_mark
order by g.grade desc, 1 nulls last;