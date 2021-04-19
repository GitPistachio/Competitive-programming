/*
* Project name : HackerRank: Higher Than 75 Marks
* Link         : https://www.hackerrank.com/challenges/more-than-75-marks/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-19
* Description  :
* Status       : Accepted (209567823)
* Tags         : sql
* Comment      : 
*/

select 
    name
from STUDENTS
where marks > 75
order by substr(name, length(name) - 2, 3), id;