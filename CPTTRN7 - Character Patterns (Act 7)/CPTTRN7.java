/*
* Project name : SPOJ: CPTTRN7 - Character Patterns (Act 7)
* Author       : Wojciech Raszka
* Date created : 2019-02-23
* Description  :
* Status       : Accepted (23286557)
* Tags         : java, console pattern, diamond
* Comment      :
*/

import java.lang.StringBuilder;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class CPTTRN7{
  public static StringBuilder diamondRow(int s, int row){
    StringBuilder sb = new StringBuilder();

    if (row < s){
      for (int i=0; i < s - row - 1; i++){
        sb.append(".");
      }

      sb.append("/");

      for (int i=s - row; i < s + row; i++){
        sb.append(".");
      }

      sb.append("\\");

      for (int i=s + row + 1; i < 2*s; i++){
        sb.append(".");
      }
    } else if (row < 2*s){
      for (int i=0; i < row - s; i++){
        sb.append(".");
      }

      sb.append("\\");

      for (int i=row - s + 1; i < 3*s - row - 1; i++){
        sb.append(".");
      }

      sb.append("/");

      for (int i=3*s - row; i < 2*s; i++){
        sb.append(".");
      }
    }

    return sb;
  }

  public static void diamondGrid(int r, int c, int s) {
    StringBuilder dg = new StringBuilder();
    StringBuilder sb;
    for (int i = 0; i < 2*s; i++){
      sb = diamondRow(s, i);
      for (int j = 0; j < c; j++){
        dg.append(sb);
      }
      dg.append("\n");
    }
    sb = new StringBuilder(dg);
    for (int i = 0; i < r - 1; i++){
      dg.append(sb);
    }
    System.out.print(dg.toString());
  }

  public static void main(String args[]) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int t, r, c, s;
    String[] p;

    t = Integer.parseInt(br.readLine());

    for (int i=0; i < t; i++){
      p = br.readLine().split(" ");
      r = Integer.parseInt(p[0]);
      c = Integer.parseInt(p[1]);
      s = Integer.parseInt(p[2]);

      diamondGrid(r, c, s);

      if (i + 1 < t){
        System.out.println();
      }
    }
  }
}
