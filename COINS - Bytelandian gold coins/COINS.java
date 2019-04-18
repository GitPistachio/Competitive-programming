/*
* Project name : SPOJ: COINS - Bytelandian gold coins
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-04-12
* Description  :
* Status       : Accepted (23625487)
* Tags         : java, dynamic programming
* Comment      :
*/

import java.util.Scanner;

final class COINS{
  public static long solve(int n, int k, long[] A){
    if (n < k) return A[n];

    return solve(n/2, k, A) + solve(n/3, k, A) + solve(n/4, k, A);
  }

  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int n;
    final int MAX_DP = 10000;
    long[] A = new long[MAX_DP];

    for (int i = 1; i < 12; i++){
        A[i] = i;
    }

    for (int i = 12; i < MAX_DP; i++){
        A[i] = solve(i, i - 1, A);
    }

    while (sc.hasNextInt()){
        n = sc.nextInt();
        System.out.println(solve(n, MAX_DP, A));
    }
  }
}
