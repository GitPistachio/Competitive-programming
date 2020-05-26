/*
* Project name : SPOJ: MAJSTOR - Majstor
* Author       : Wojciech Raszka
* Date created : 2019-02-15
* Description  :
* Status       : Accepted (23238652)
* Comment      :
*/

import java.util.Scanner;

class MAJSTOR{
  static int rmr(int S, int P, int R){
    int mp = S + 2*P;

    if (P + 2*R > mp)
      mp = P + 2*R;

    if (R + 2*S > mp)
      mp = R + 2*S;

    return mp;
  }

  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int R = sc.nextInt(), N, p = 0, mp = 0;
    char[] sa, oa;
    int[][] oh = new int[50][4];

    sc.nextLine();
    sa = sc.nextLine().toCharArray();
    N = sc.nextInt();
    sc.nextLine();

    for (int n=0; n < N; n++){
      oa = sc.nextLine().toCharArray();
      for (int i=0; i < R; i++){
        if (sa[i] == oa[i])
          p++;
        if ((sa[i] == 'S' && oa[i] == 'P') || (sa[i] == 'R' && oa[i] == 'S') || (sa[i] == 'P' && oa[i] == 'R'))
          p += 2;

        oh[i][oa[i] - 80]++;
      }
    }
    for (int i=0; i < R; i++)
      mp += rmr(oh[i][0], oh[i][2], oh[i][3]);
    System.out.println(p + "\n" + mp);
  }
}
