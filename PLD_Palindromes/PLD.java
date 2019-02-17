/*
* Project name : SPOJ: Palindromes
* Author       : Wojciech Raszka
* Date created : 2019-??-??
* Description  :
* Status       : Accepted (???)
* Comment      :
*/


import java.util.Scanner;

class PLD_v4{
  static final int M1 = 1000000007;
  static final int M2 = 10000019;
  static final int H1 = 999983;
  static final int H2 = 99991;

  public static void hashing(char[] str, int n, int K, long[] hash_T1, long[] hash_T2){
    long d1 = 1, d2 = 1;
    long T1 = 0, T2 = 0;

    for (int i=1; i < K; i++){
      d1 = (d1*H1) % M1;
      d2 = (d2*H2) % M2;
    }

    for (int i=0; i < K; i++){
      T1 = (T1*H1 + str[i]) % M1;
      T2 = (T2*H2 + str[i]) % M2;
    }

    for (int i=0; i < n - K; i++){
      hash_T1[i] = T1;
      hash_T2[i] = T2;

      T1 = ((T1 - d1*str[i])*H1 + str[i + K]) % M1;
      T1 = (T1 + M1) % M1;

      T2 = ((T2 - d2*str[i])*H2 + str[i + K]) % M2;
      T2 = (T2 + M2) % M2;
    }
    hash_T1[n - K] = T1;
    hash_T2[n - K] = T2;
  }

  public static void reversed_hashing(char[] str, int n, int K, long[] rev_hash_T1, long[] rev_hash_T2){
    long d1 = 1, d2 = 1;
    long T1 = 0, T2 = 0;

    for (int i=1; i < K; i++){
      d1 = (d1*H1) % M1;
      d2 = (d2*H2) % M2;
    }

    for (int i=0; i < K; i++){
      T1 = (T1*H1 + str[n - i - 1]) % M1;
      T2 = (T2*H2 + str[n - i - 1]) % M2;
    }

    for (int i=0; i < n - K; i++){
      rev_hash_T1[i] = T1;
      rev_hash_T2[i] = T2;

      T1 = ((T1 - d1*str[n - i - 1])*H1 + str[n - i - K - 1]) % M1;
      T1 = (T1 + M1) % M1;

      T2 = ((T2 - d2*str[n - i - 1])*H2 + str[n - i - K - 1]) % M2;
      T2 = (T2 + M2) % M2;
    }
    rev_hash_T1[n - K] = T1;
    rev_hash_T2[n - K] = T2;
  }

  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int K = sc.nextInt(); sc.nextLine();

    char[] str = sc.nextLine().toCharArray();

    int n = str.length;

    long[] hash_T1 = new long[n];
    long[] hash_T2 = new long[n];
    hashing(str, n, K, hash_T1, hash_T2);

    long[] rev_hash_T1 = new long[n];
    long[] rev_hash_T2 = new long[n];
    reversed_hashing(str, n, K, rev_hash_T1, rev_hash_T2);

    int no_of_pld = 0;
    int j;
    for (int i=0; i <= n - K; i++){
      j = n - i - K;
      if (hash_T1[i] == rev_hash_T1[j] && hash_T2[i] == rev_hash_T2[j])
        no_of_pld++;
    }

    System.out.println(no_of_pld);
  }
}
