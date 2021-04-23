/*
* Project name : HackerRank: Occupations
* Link         : https://www.hackerrank.com/challenges/occupations/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-23
* Description  :
* Status       : Accepted (210119565)
* Tags         : sql
* Comment      : 
*/

select doctor, professor, singer, actor
from
(
    select
       name
     , occupation
     , row_number() over (partition by occupation order by name) position
    from occupations
)
pivot
(
  min(name)
  for occupation in ('Doctor' doctor, 'Professor' professor, 'Singer' singer, 'Actor' actor)
)
order by doctor, professor, singer, actor;