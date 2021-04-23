/*
* Project name : HackerRank: Symmetric Pairs
* Link         : https://www.hackerrank.com/challenges/symmetric-pairs/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-23
* Description  :
* Status       : Accepted (210143145)
* Tags         : sql
* Comment      : 
*/

with FUNCTIONS_ as
(
    select row_number() over (order by X, Y) id, X, Y
    from Functions
)
select distinct f.X, f.Y
from FUNCTIONS_ f
where f.X <= f.Y
    and exists (select * from FUNCTIONS_ sf where sf.Y = f.X and sf.X = f.Y and sf.id <> f.id)
order by f.X;