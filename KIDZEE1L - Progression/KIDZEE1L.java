/*
* Project name : SPOJ: KIDZEE1L - Progression
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-01
* Description  :
* Status       : Accepted (23862377)
* Tags         : java, arithmetic progression, geometric progression
* Comment      :
*/

import java.util.Scanner;

class KIDZEE1L{
  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int T = sc.nextInt();
    int a, b, c;

    for (int t = 1; t <= T; t++){
      a = sc.nextInt();
      b = sc.nextInt();
      c = sc.nextInt();

      System.out.print("Case " + t + ": ");
      if (c - b - b + a == 0 ){
        if (b*b - a*c == 0){
            System.out.println("Both");
        } else {
          System.out.println("Arithmetic Progression");
        }
      } else if (b*b - a*c == 0){
          System.out.println("Geometric Progression");
      } else {
        System.out.println("None");
      }
    }
  }
}
