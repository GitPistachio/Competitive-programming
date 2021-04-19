/*
* Project name : HackerRank: Employee Salaries
* Link         : https://www.hackerrank.com/challenges/salary-of-employees/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-19
* Description  :
* Status       : Accepted (209568295)
* Tags         : sql
* Comment      : 
*/

select 
    name
from EMPLOYEE
where salary > 2000
    and months < 10
order by employee_id;