/*
* Project name : SPOJ: QWERTY03 - Java counting
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-03-29
* Description  :
* Status       : Accepted (23522982)
* Tags         : java
* Comment      : 237 chars
*/

import java.util.*;class E{public static void main(String a[]){Scanner s=new Scanner(System.in);int n=s.nextInt()+1;int[] l=new int[256];while(n-->1)l[s.next().charAt(0)]++;for(;n<123;n++)if(l[n]>0)System.out.println((char)n+" "+l[n]);}}
