/*
* Project name : SPOJ: UFPR14D - Inquire
* Author       : Wojciech Raszka
* Date created : 2019-02-16
* Description  :
* Status       : Accepted (23241700)
* Comment      :
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class UFPR14D{
  public static void main(String args[]) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    String[] P, AB;
    int N, Q;
    int k, l;
    int[] agg;

    N = Integer.parseInt(br.readLine());
    agg = new int[N + 1];

    P = br.readLine().split(" ");

    agg[1] = Integer.parseInt(P[0]);
    for (int i = 1; i < N; i++){
        agg[i + 1] = agg[i] + Integer.parseInt(P[i]);
    }

    Q = Integer.parseInt(br.readLine());

    for (int i = 0; i < Q; i++){
      AB = br.readLine().split(" ");
      k = Integer.parseInt(AB[0]);
      l = Integer.parseInt(AB[1]);
      System.out.println(agg[l] - agg[k - 1]);
    }
  }
}
