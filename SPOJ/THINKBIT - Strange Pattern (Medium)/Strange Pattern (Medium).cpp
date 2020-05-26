/*
* Project name : SPOJ: THINKBIT - Strange Pattern (Medium)
* Author       : Wojciech Raszka
* Date created : 2019-03-30
* Description  :
* Status       : Accepted (23530958)
* Tags         : c++
* Comment      : I think there is much more elegant solution
*/



#include <stdio.h>

int count(int x){

 return x>>13&1|x>>12&1|x>>11&1|x>>10&1|x>>9&1|x>>8&1|x>>7&1|x>>6&1|x>>5&1|x>>4&1|x>>3&1|x>>2&1|x>>1&1|2;

}

int main(){for(int i=1;i^10001;i++)printf("%d %d\n",i,count(i));return 0;}
