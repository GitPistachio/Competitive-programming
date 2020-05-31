/*
* Project name : SPOJ: ACPC10A - What’s Next
* Author       : Wojciech Raszka
* Date created : 2019-02-10
* Description  :
* Status       : Accepted (23206155)
* Comment      :
*/

import java.util.Scanner;

class ACPC10A{
  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int a, b, c;

    a = sc.nextInt();
    b = sc.nextInt();
    c = sc.nextInt();
    while (a != 0 || b != 0 || c != 0){
      if (b - a == c - b){
        System.out.println("AP " + (c + b - a));
      } else if (b*b == a*c) {
        System.out.println("GP " + (c*b/a));
      }

      a = sc.nextInt();
      b = sc.nextInt();
      c = sc.nextInt();
    }
  }
}
