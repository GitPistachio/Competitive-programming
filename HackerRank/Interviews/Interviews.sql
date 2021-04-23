/*
* Project name : HackerRank: Interviews
* Link         : https://www.hackerrank.com/challenges/interviews/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-23
* Description  :
* Status       : Accepted (210153548)
* Tags         : sql
* Comment      : 
*/

with VIEW_STATS_ as
(
    select challenge_id, sum(total_views) total_views, sum(total_unique_views) total_unique_views 
    from View_Stats vs
    group by challenge_id
), SUBMISSIONS_STATS_ as
(
    select challenge_id, sum(total_submissions) total_submissions, sum(total_accepted_submissions) total_accepted_submissions
    from Submission_Stats ss
    group by challenge_id
), CONTEST_STATS_ as
(
    select contest_id
        , nvl(sum(total_views), 0) total_views
        , nvl(sum(total_unique_views), 0) total_unique_views
        , nvl(sum(total_submissions), 0) total_submissions
        , nvl(sum(total_accepted_submissions), 0) total_accepted_submissions
    from Colleges cl
        left join Challenges c on c.college_id = cl.college_id
        left join VIEW_STATS_ vs on vs.challenge_id = c.challenge_id
        left join SUBMISSIONS_STATS_ ss on ss.challenge_id = c.challenge_id
    group by contest_id
)
select c.contest_id, c.hacker_id, c.name, total_submissions, total_accepted_submissions, total_views, total_unique_views
from CONTEST_STATS_  cs
    inner join Contests c on c.contest_id = cs.contest_id
where total_submissions <> 0 or total_accepted_submissions <> 0 or total_views <> 0 or total_unique_views <> 0
order by contest_id
;