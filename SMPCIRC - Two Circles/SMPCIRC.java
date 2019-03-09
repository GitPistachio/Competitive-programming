/*
* Project name : SPOJ: SMPCIRC - Two Circles
* Author       : Wojciech Raszka
* Date created : 2019-02-24
* Description  :
* Status       : Accepted (23290472)
* Comment      :
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class SMPCIRC{
  public static int squareDistance(int x1, int y1, int x2, int y2){
    return (x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1);
  }
  public static void main(String args[]) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int T = Integer.parseInt(br.readLine());
    int x1, y1, r1, x2, y2, r2;
    int sd, dr;
    String[] tokens;

    for (int t = 0; t < T; t++){
      tokens = br.readLine().split(" ");
      x1 = Integer.parseInt(tokens[0]);
      y1 = Integer.parseInt(tokens[1]);
      r1 = Integer.parseInt(tokens[2]);
      x2 = Integer.parseInt(tokens[3]);
      y2 = Integer.parseInt(tokens[4]);
      r2 = Integer.parseInt(tokens[5]);

      sd = squareDistance(x1, y1, x2, y2);
      dr  = r2 - r1;
      if (sd < dr*dr){
        System.out.println("I");
      } else if (sd == dr*dr){
        System.out.println("E");
      } else {
        System.out.println("O");
      }
    }
  }
}
