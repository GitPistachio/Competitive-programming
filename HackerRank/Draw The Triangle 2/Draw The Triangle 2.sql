/*
* Project name : HackerRank: Draw The Triangle 2
* Link         : https://www.hackerrank.com/challenges/draw-the-triangle-2/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-20
* Description  :
* Status       : Accepted (209730026)
* Tags         : sql, drawing of a triangle
* Comment      : 
*/

select rpad('*', level*2, ' *')
from dual
connect by level <= 20;