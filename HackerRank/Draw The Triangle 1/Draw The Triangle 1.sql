/*
* Project name : HackerRank: Draw The Triangle 1
* Link         : https://www.hackerrank.com/challenges/draw-the-triangle-1/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-20
* Description  :
* Status       : Accepted (209729820)
* Tags         : sql, drawing of a triangle
* Comment      : 
*/

select rpad('*', 41 - level*2, ' *')
from dual
connect by level <= 20;