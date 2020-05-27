/*
* Project name : SPOJ: SMPDIV - Divisibility
* Author       : Wojciech Raszka
* Date created : 2019-02-24
* Description  :
* Status       : Accepted (23290839)
* Comment      :
*/

import java.util.Scanner;
import java.lang.StringBuilder;

class SMPDIV{
  public static void div(int n, int x, int y){
    StringBuilder sb = new StringBuilder();
    int a = 0;

    for (int i = 0; i < n/x; i++){
      a += x;
      if (a % y != 0 && a < n){
        sb.append(a);
        sb.append(" ");
      }
    }
    sb.setLength(sb.length() - 1);
    sb.append("\n");
    System.out.print(sb.toString());
  }
  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);

    int T = sc.nextInt();
    int n, x, y;

    for (int t = 0; t < T; t++){
      n = sc.nextInt();
      x = sc.nextInt();
      y = sc.nextInt();

      div(n, x, y);
    }
  }
}
