/*
* Project name : SPOJ: Arithmetic or Geometric ?
* Author       : Wojciech Raszka
* Date created : 2019-02-10
* Description  :
* Status       :
* Comment      :
*/

import java.util.Scanner;
import java.lang.Math;

class ARIORGEO{
  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int T = sc.nextInt();
    double a, b, c;
    double e = 0.000000000000001;

    for (int t = 0; t < T; t++){
      a = sc.nextDouble();
      b = sc.nextDouble();
      c = sc.nextDouble();

      if (Math.abs(c - b - b + a) < e){
        if (Math.abs(b*b - a*c) < e){
            System.out.println("Both");
        } else {
          System.out.println("Arithmetic");
        }
      } else if (Math.abs(b*b - a*c) < e){
          System.out.println("Geometric");
      } else {
        System.out.println("None");
      }
    }
  }
}
