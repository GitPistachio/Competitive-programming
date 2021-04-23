/*
* Project name : HackerRank: New Companies
* Link         : https://www.hackerrank.com/challenges/the-company/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-23
* Description  :
* Status       : Accepted (210124718)
* Tags         : sql
* Comment      : 
*/

select c.company_code, c.founder, NVL(lm.no, 0), NVL(sm.no, 0), NVL(m.no, 0),  NVL(e.no, 0)
from Company c
  left join 
  (
    select company_code, count(distinct lead_manager_code) no
    from Lead_Manager
    group by company_code
  ) lm on lm.company_code = c.company_code
  left join 
  (
    select company_code, count(distinct senior_manager_code) no
    from Senior_Manager
    group by company_code
  ) sm on sm.company_code = c.company_code
  left join 
  (
    select company_code, count(distinct manager_code) no
    from Manager
    group by company_code
  ) m on m.company_code = c.company_code
  left join 
  (
    select company_code, count(distinct employee_code) no
    from Employee
    group by company_code
  ) e on e.company_code = c.company_code
order by c.company_code;