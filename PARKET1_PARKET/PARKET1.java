/*
* Project name : SPOJ: PARKET1 - Parkiet
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-02-11
* Description  :
* Status       : Accepted (23212744)
* Tags         : java
* Comment      : Solve equation L*D = R + B and (l-2)*(D-2) = B
*/

import java.util.Scanner;
import java.lang.Math;

class PARKET1{
  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int R, B, L, D;
    int delta;

    R = sc.nextInt();
    B = sc.nextInt();

    delta = (R + 4)*(R + 4) - 16*(R + B);

    L = (int)(((R + 4) + Math.sqrt(delta))/4);
    D = (int)(((R + 4) - Math.sqrt(delta))/4);

    System.out.println(L + " " + D);
  }
}
