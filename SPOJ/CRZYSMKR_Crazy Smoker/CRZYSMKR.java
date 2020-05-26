/*
* Project name : SPOJ: CRZYSMKR - Crazy Smoker
* Author       : Wojciech Raszka
* Date created : 2019-03-08
* Description  :
* Status       : Accepted (23367626)
* Comment      : Formula transform to (30*N) mod 11
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class CRZYSMKR{
  public static void main(String args[]) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int T = Integer.parseInt(br.readLine());
    long N, C;

    for (int t = 0; t < T; t++){
      N = Long.parseLong(br.readLine());;
      C = (30*N) % 11;
      if (C > 0){
          System.out.println(11 - C);
      } else {
        System.out.println(0);
      }
    }
  }
}
