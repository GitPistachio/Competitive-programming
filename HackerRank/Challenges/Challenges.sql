/*
* Project name : HackerRank: Challenges
* Link         : https://www.hackerrank.com/challenges/harry-potter-and-wands/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-22
* Description  :
* Status       : Accepted (210032508)
* Tags         : sql
* Comment      : 
*/

with HACKERS_CHALLENGES_ as
(
    select 
        h.hacker_id
      , h.name
      , count(*) no_of_solved_challenges
      , max(count(*)) over () max_no_of_solved_challanges
      , count(h.hacker_id) over (partition by count(*)) no_of_hackers
    from Hackers h
        inner join Challenges c on c.hacker_id = h.hacker_id
    group by h.hacker_id, h.name
)
select hacker_id, name, no_of_solved_challenges
from HACKERS_CHALLENGES_
where no_of_solved_challenges = max_no_of_solved_challanges
    or no_of_hackers = 1
order by no_of_solved_challenges desc, hacker_id;