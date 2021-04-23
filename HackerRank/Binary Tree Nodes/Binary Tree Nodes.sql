/*
* Project name : HackerRank: Binary Tree Nodes
* Link         : https://www.hackerrank.com/challenges/binary-search-tree-1/problem
* Try it on    : 
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2021-04-23
* Description  :
* Status       : Accepted (210122016)
* Tags         : sql
* Comment      : 
*/

select 
      b.n
    , case 
        when b.p is null then 'Root'
        when exists (select * from BST c where c.p = b.n) then 'Inner'
        else 'Leaf'
      end
from BST b
order by b.n;