/*
* Project name : HackerRank: Type of Triangle
* Link         : https://www.hackerrank.com/challenges/average-population-of-each-continent/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-19
* Description  :
* Status       : Accepted (209571449)
* Tags         : sql, triangle
* Comment      : 
*/

select
    case 
        when a = b and b = c then 'Equilateral'
        when a + b <= c or a + c <= b or b + c <= a then 'Not A Triangle'
        when a = b or a = c or b = c then 'Isosceles'
        else 'Scalene'
    end
from TRIANGLES;