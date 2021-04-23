/*
* Project name : HackerRank: 15 Days of Learning SQL
* Link         : https://www.hackerrank.com/challenges/15-days-of-learning-sql/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-23
* Description  :
* Status       : Accepted (210150495)
* Tags         : sql
* Comment      : 
*/

with SUBMISSIONS_ as
(
    select 
          s.submission_date
        , s.submission_date - min(submission_date) over () + 1 no_of_passed_days
        , count(*) over (partition by hacker_id order by submission_date) no_of_submited_days
        , s.hacker_id
        , count(*) no_of_submissions
        , max(count(*)) over (partition by submission_date) max_no_of_submissions
    from Submissions s
    group by s.submission_date, s.hacker_id
)
select submission_date, no_of_hackers, r.hacker_id, h.name
from
(
    select 
        submission_date
      , sum(case when no_of_passed_days = no_of_submited_days then 1 else 0 end) no_of_hackers
      , min(case when no_of_submissions = max_no_of_submissions then hacker_id end) hacker_id
    from SUBMISSIONS_ s
    group by submission_date
) r
    inner join Hackers h on h.hacker_id = r.hacker_id
order by 1;