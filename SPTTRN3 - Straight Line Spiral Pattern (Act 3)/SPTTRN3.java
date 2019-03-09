/*
* Project name : SPOJ: SPTTRN3 - Straight Line Spiral Pattern (Act 3)
* Author       : Wojciech Raszka
* Date created : 2019-02-25
* Description  :
* Status       : Accepted (23298598)
* Comment      :
*/

import java.util.Scanner;

class SPTTRN3{
  public static void drawMaize(int s){
    boolean[][] maize = new boolean[s][s];
    int i = 1, j = -1, r = s - 1;
    boolean move, normal = true, right = true;

    do {
      move = true;
      if (right){
        if (j + 1 < r){
          j++;
          if (normal){
            maize[i][j] = true;
          } else {
            maize[j][i] = true;
          }
        } else if (i + 1 < r){
          i++;
          if (normal){
            maize[i][j] = true;
          } else {
            maize[j][i] = true;
          }
        } else if (j > s - r) {
          j--;
          if (normal){
            maize[i][j] = true;
          } else {
            maize[j][i] = true;
          }
          right = false;
        } else {
          move = false;
        }
      } else {
        if (j > s - r){
          j--;
          if (normal){
            maize[i][j] = true;
          } else {
            maize[j][i] = true;
          }
        } else if (i > s - r + 2) {
          i--;
          if (normal){
            maize[i][j] = true;
          } else {
            maize[j][i] = true;
          }
        } else if (j + 1 < r - 2){
          j++;
          normal = ! normal;
          if (normal){
            maize[i][j] = true;
          } else {
            maize[j][i] = true;
          }
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
