/*
* Project name : SPOJ: Character patterns (Act 8)
* Author       : Wojciech Raszka
* Date created : 2019-02-09
* Description  :
* Status       : Accepted (23198165)
* Comment      :
*/

import java.util.Scanner;

class CPTTRN8{
  public static String diamondRow(int s, int row){
    String diamond_row = "";

    if (row < s){
      for (int i=0; i < s - row - 1; i++){
        diamond_row += ".";
      }

      diamond_row += "/";

      for (int i=s - row; i < s + row; i++){
        diamond_row += "*";
      }

      diamond_row += "\\";

      for (int i=s + row + 1; i < 2*s; i++){
        diamond_row += ".";
      }
    } else if (row < 2*s){
      for (int i=0; i < row - s; i++){
        diamond_row += ".";
      }

      diamond_row += "\\";

      for (int i=row - s + 1; i < 3*s - row - 1; i++){
        diamond_row += "*";
      }

      diamond_row += "/";

      for (int i=3*s - row; i < 2*s; i++){
        diamond_row += ".";
      }
    }

    return diamond_row;
  }

  public static void diamondGrid(int r, int c, int s){
    String diamond_row;
    String newline = System.lineSeparator();
    for (int i=0; i < r; i++){
      for (int row=0; row < 2*s; row++){
        diamond_row = diamondRow(s, row);
        for (int j=0; j < c; j++){
          System.out.print(diamond_row);
        }
        System.out.print(newline);
      }
    }
  }

  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int t, r, c, s;

    t = sc.nextInt();

    for (int i=0; i < t; i++){
      r = sc.nextInt();
      c = sc.nextInt();
      s = sc.nextInt();

      diamondGrid(r, c, s);
    }
  }
}
