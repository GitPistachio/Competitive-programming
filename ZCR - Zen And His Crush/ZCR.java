/*
* Project name : SPOJ: ZCR - Zen And His Crush
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-02-21
* Description  :
* Status       : Accepted (23279078)
* Tags         : java, math, probability theory, dynamic-programming, probability of k heads from n simultaneously tossed biased coins
* Comment      : O(n*k) See: P(n, k) = P(n - 1, k)*(1 - p_n) + P(n - 1,k - 1)*p_n
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class ZCR{
  public static void setProbabilityMatrix(int N, int K, double p[], double P[][]){
    P[0][0] = 1;
    for (int i = 0; i < N; i++){
      P[i + 1][0] = P[i][0]*(1 - p[i]);
      for (int j = 1; j <= i + 1 && j <= K; j++){
        P[i + 1][j] = P[i][j]*(1 - p[i]) + P[i][j - 1]*p[i];
      }
    }
  }

  public static void main(String args[]) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int T = Integer.parseInt(br.readLine());
    String[] NK, prob;
    int N, K;
    double[] p = new double[1000];
    double[][] P = new double[1001][1001];

    for (int t = 0; t < T; t++){
      NK = br.readLine().split(" ");
      N = Integer.parseInt(NK[0]);
      K = Integer.parseInt(NK[1]);

      prob = br.readLine().split(" ");
      for (int i = 0; i < N; i++){
        p[i] = Double.parseDouble(prob[i]);
      }

      setProbabilityMatrix(N, K, p, P);

      System.out.println(String.format("%.10f", P[N][K]));
    }
  }
}
