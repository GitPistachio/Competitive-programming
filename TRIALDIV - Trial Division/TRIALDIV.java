/*
* Project name : SPOJ: TRIALDIV - Trial Division
* Author       : Wojciech Raszka
* Date created : 2019-02-24
* Description  :
* Status       : Accepted (23289395)
* Comment      :
*/

import java.lang.StringBuilder;
import java.util.Scanner;
import java.lang.Math;

class TRIALDIV{
  public static void primeFactors(int n){
    StringBuilder sb = new StringBuilder();
    while (n % 2 == 0){
      sb.append("2 ");
      n /= 2;
    }

    for (int i = 3; i <= Math.sqrt(n); i += 2){
      while (n % i == 0){
        sb.append(i);
        sb.append(" ");
        n /= i;
      }
    }

    if (n > 2){
      sb.append(n);
      sb.append("\n");
      System.out.print(sb.toString());
    } else if (sb.length() > 0){
        sb.setLength(sb.length() - 1);
        sb.append("\n");
        System.out.print(sb.toString());
    } else {
      System.out.print("\n");
    }
  }

  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);

    int T = sc.nextInt();
    int n;

    for (int t = 0; t < T; t++){
      n = sc.nextInt();
      primeFactors(n);
    }
  }
}
