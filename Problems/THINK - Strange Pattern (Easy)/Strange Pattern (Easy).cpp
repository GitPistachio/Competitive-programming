/*
* Project name : SPOJ: THINK - Strange Pattern (Easy)
* Author       : Wojciech Raszka
* Date created : 2019-03-30
* Description  :
* Status       : Accepted (23427021)
* Tags         : c++
* Comment      :
*/


    #include <stdio.h>

    int count(int x){

     return 2+x/2-(x-2)/2;

    }

    int main(){

     for( int i=1 ; i-1001 ; i++ ) printf("%d %d\n",i,count(i));

     return 0;

    }
