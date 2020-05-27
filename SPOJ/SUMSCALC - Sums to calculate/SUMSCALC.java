/*
* Project name : SPOJ: SUMSCALC - Sums to calculate
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-02-24
* Description  :
* Status       : Accepted (23289730)
* Tags         : java, fast I/O, sum of odd number A005408 (OEIS), sum of even numbers A005843 (OEIS), sum of squares A000290 (OEIS), sum of cubes A000578 (OEIS)
* Comment      :
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class SUMSCALC{
  public static void main(String args[]) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int T = Integer.parseInt(br.readLine());
    long n;
    long S, S_odd, S_even, S_square, S_cube;

    for (int t = 0; t < T; t++){
      n = Long.parseLong(br.readLine());
      S = ((n + 1)*n) >> 1;
      S_odd = S << 1;
      S_even = S_odd - n;
      S_square = 0;
      S_cube = 0;
      for (long i = 1; i <= n; i++){
        S_square += i*i;
        S_cube += i*i*i;
      }
      System.out.println(S + " " + S_odd + " " + S_even + " " + S_square + " " + S_cube);
    }
  }
}
