/*
* Project name : SPOJ: ABSP1 - abs(a-b) I
* Author       : Wojciech Raszka
* Date created : 2019-02-13
* Description  :
* Status       : Accepted (23224729)
* Tags         : java
* Comment      : Use the formula (A[i+1] - A[i])*(N - i - 1)*(i + 1) for all N > i > 0
*/

import java.util.Scanner;

class ABSP1{
  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int T, N;
    long a, b, sum_of_diffs;

    T = sc.nextInt();
    for (int t=0; t < T; t++){
      N = sc.nextInt();

      sum_of_diffs = 0;
      a = sc.nextLong();
      for (int n=1; n < N; n++){
        b = sc.nextLong();
        sum_of_diffs += (b - a)*(N - n)*n;
        a = b;
      }
      System.out.println(sum_of_diffs);
    }
  }
}
