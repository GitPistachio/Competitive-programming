/*
* Project name : SPOJ: SPTTRN1 - Straight Line Spiral Pattern (Act 1)
* Author       : Wojciech Raszka
* Date created : 2019-02-24
* Description  :
* Status       : Accepted (23292140)
* Comment      :
*/

import java.util.Scanner;

class SPTTRN1{
  public static void drawMaize(int s){
    boolean[][] maize = new boolean[s][s];
    int i = 1, j = -1, r = s - 1;
    boolean move, right = true;

    do {
      move = true;
      if (right){
        if (j + 1 < r){
          j++;
          maize[i][j] = true;
        } else if (i + 1 < r){
          i++;
          maize[i][j] = true;
        } else if (j > s - r) {
          j--;
          maize[i][j] = true;
          right = false;
        } else {
          move = false;
        }
      } else {
        if (j > s - r){
          j--;
          maize[i][j] = true;
        } else if (i > s - r + 2) {
          i--;
          maize[i][j] = true;
        } else if (j + 1 < r - 2){
          j++;
          maize[i][j] = true;
          right = true;
          r -= 2;
        } else {
          move = false;
        }
      }
    } while (move);

    for (i = 0; i < s; i++){
      for (j = 0; j < s; j++){
        if (maize[i][j]){
          System.out.print(".");
        } else {
          System.out.print("*");
        }
      }
      System.out.print("\n");
    }
  }
  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);

    int T = sc.nextInt();

    for (int t = 0; t < T; t++){
      drawMaize(sc.nextInt());
      if (t + 1 < T){
        System.out.print("\n");
      }
    }
  }
}
