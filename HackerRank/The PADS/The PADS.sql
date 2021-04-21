/*
* Project name : HackerRank: The PADS
* Link         : https://www.hackerrank.com/challenges/the-pads/submissions/code/209839952
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-21
* Description  :
* Status       : Accepted (209838956)
* Tags         : sql, manhattan distance
* Comment      : 
*/

select name || '(' || substr(occupation, 1, 1) || ')'
from OCCUPATIONS
order by name;
select 'There are a total of ' || count(*) || ' ' || lower(occupation) || 's.'
from OCCUPATIONS
group by occupation
order by count(*), occupation;