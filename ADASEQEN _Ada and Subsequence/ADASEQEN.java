/*
* Project name : SPOJ: ADASEQEN - Ada and Subsequence
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-02-17
* Description  :
* Status       : Accepted (23247921)
* Tags         : java, longest common subsequence, dynamic programming
* Comment      : Longest common subsequence with weights
*/

import java.util.Scanner;

class ADASEQEN{
  static int longestWeightedCommonSubsequence(String str1, String str2, int weights[]){
    int n = str1.length(), m = str2.length();
    int[][] C = new int[n + 1][m + 1];

    for (int i = 0; i < n; i++){
      for (int j = 0; j < m; j++){
        if (str1.charAt(i) == str2.charAt(j)){
          C[i + 1][j + 1] = C[i][j] + weights[str1.charAt(i) - 97];
        } else if (C[i][j + 1] > C[i + 1][j]) {
          C[i + 1][j + 1] = C[i][j + 1];
        } else {
          C[i + 1][j + 1] = C[i + 1][j];
        }
      }
    }

    return C[n][m];
  }

  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt(), m = sc.nextInt();
    int[] weights = new int[26];
    String str1, str2;

    for (int i = 0; i < 26; i++){
      weights[i] = sc.nextInt();
    }
    sc.nextLine();
    str1 = sc.nextLine();
    str2 = sc.nextLine();

    System.out.println(longestWeightedCommonSubsequence(str1, str2, weights));
  }
}
