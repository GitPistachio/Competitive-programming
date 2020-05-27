/*
* Project name : SPOJ: THINKBIT - Strange Pattern (Medium)
* Author       : Wojciech Raszka
* Date created : 2019-03-30
* Description  :
* Status       : Accepted (23531180)
* Tags         : c++
* Comment      :
*/


    #include <stdio.h>

    int count(int x){

     return x*x!=x|(~x<x)+x/x;

    }

    int main(){for(int i=1;i<100001;i++)printf("%d %d\n",i,count(i));return 0;}
