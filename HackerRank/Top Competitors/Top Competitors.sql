/*
* Project name : HackerRank: Top Competitors
* Link         : https://www.hackerrank.com/challenges/full-score/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-22
* Description  :
* Status       : Accepted (209979359)
* Tags         : sql
* Comment      : 
*/

select h.hacker_id, h.name
from Hackers h
    inner join Submissions s on s.hacker_id = h.hacker_id
    inner join Challenges c on c.challenge_id = s.challenge_id
    inner join Difficulty d on d.difficulty_level = c.difficulty_level 
group by h.hacker_id, h.name
having sum(case when s.score = d.score then 1 else 0 end) > 1
order by sum(case when s.score = d.score then 1 else 0 end) desc, h.hacker_id;