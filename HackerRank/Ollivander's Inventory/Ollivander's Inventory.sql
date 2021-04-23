/*
* Project name : HackerRank: Ollivander's Inventory
* Link         : https://www.hackerrank.com/challenges/harry-potter-and-wands/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-22
* Description  :
* Status       : Accepted (210030760)
* Tags         : sql
* Comment      : 
*/

select w.id, wp.age, w.coins_needed, w.power
from Wands w
    inner join Wands_Property wp on wp.code = w.code
    inner join 
(
    select wp.age, w.power, min(coins_needed) min_coins_needed
    from Wands w
        inner join Wands_Property wp on wp.code = w.code
    where wp.is_evil = 0
    group by wp.age, w.power
) d on wp.age = d.age and w.power = d.power and d.min_coins_needed = w.coins_needed
order by w.power desc, wp.age desc;