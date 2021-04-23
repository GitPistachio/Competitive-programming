/*
* Project name : HackerRank: Contest Leaderboard
* Link         : https://www.hackerrank.com/challenges/contest-leaderboard/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-23
* Description  :
* Status       : Accepted (210131493)
* Tags         : sql
* Comment      : 
*/

select h.hacker_id, h.name, sum(s.best_score) total_score
from Hackers h
    inner join 
    (
      select hacker_id, max(score) best_score
      from Submissions
      group by hacker_id, challenge_id
    ) s on s.hacker_id = h.hacker_id
group by h.hacker_id, h.name
having sum(s.best_score) > 0
order by total_score desc, h.hacker_id;