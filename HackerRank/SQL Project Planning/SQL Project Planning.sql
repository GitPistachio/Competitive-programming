/*
* Project name : HackerRank: SQL Project Planning
* Link         : https://www.hackerrank.com/challenges/sql-projects/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-23
* Description  :
* Status       : Accepted (210140868)
* Tags         : sql
* Comment      : 
*/

select min(start_date), max(end_date)
from
(
    select d.*, sum(days_between_tasks) over (order by start_date) project
    from
    (
        select p.*
            , start_date - NVL(lag(end_date, 1) over (order by p.start_date), start_date) days_between_tasks
        from Projects p
    ) d
)
group by project
order by count(*), 1;