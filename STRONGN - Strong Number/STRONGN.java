/*
* Project name : SPOJ: STRONGN - Strong Number
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-04-12
* Description  :
* Status       : Accepted (23629403)
* Tags         : java, math, integer sequence A014080 (OEIS)
* Comment      : There are only four factorions: 1, 2, 145, 40585
*/

import java.util.Scanner;

final class STRONGN{
  public static int[] F = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};

  public static boolean isStrong(long x){

    if (x > 100000000) return false;

    int factorial_sum = 0;
    int y = (int) x;
    while (y > 0){
      factorial_sum += F[y % 10];
      y /= 10;
    }

    return (factorial_sum == x);
  }
  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int T = sc.nextInt();
    long x;

    int factorial_sum;

    while (T-- > 0){
      x = sc.nextLong();

      if (isStrong(x)){
        System.out.println("YES");
      } else {
        System.out.println("NO");
      }
    }
  }
}
