/*
* Project name : SPOJ: MATHLOVE - Math is Love
* Author       : Wojciech Raszka
* Date created : 2019-02-16
* Description  :
* Status       : Accepted (23245672)
* Comment      :
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.lang.Math;

class MATHLOVE{
  static boolean isPerfectSquare(double x){
    double sqr = Math.sqrt(x);

    return ((sqr - Math.floor(sqr)) == 0);
  }

  public static void main(String args[]) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    int T = Integer.parseInt(br.readLine());
    double sqr;

    for (int t = 0; t < T; t++){
      sqr = Math.sqrt(1.0 + 8*Double.parseDouble(br.readLine()));

      if ((sqr - Math.floor(sqr)) == 0){
        System.out.println((int)((sqr - 1)/2));
      } else {
        System.out.println("NAI");
      }
    }
  }
}
