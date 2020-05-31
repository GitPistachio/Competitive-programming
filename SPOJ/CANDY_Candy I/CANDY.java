/*
* Project name : SPOJ: CANDY - Candy I
* Author       : Wojciech Raszka
* Date created : 2019-02-06
* Description  :
* Status       : Accepted (23185397)
*/

import java.util.Scanner;

class CANDY{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    short N = sc.nextShort();
    short[] pocket = new short[10000];
    int no_of_candy;
    int no_of_moves = 0;
    short avg_pocket;

    while (N != -1){
      no_of_candy = 0;
      for (short i=0; i < N; i++){
        pocket[i] = sc.nextShort();
        no_of_candy += pocket[i];
      }
      if (no_of_candy % N == 0){
        avg_pocket = (short)(no_of_candy/N);
        no_of_moves = 0;
        for (short i=0; i < N; i++){
          if (pocket[i] > avg_pocket)
              no_of_moves += pocket[i] -  avg_pocket;
        }
        System.out.println(no_of_moves);
      }
      else
        System.out.println(-1);

      N = sc.nextShort();
    }
  }
}
