/*
* Project name : SPOJ: FRNDZND - Friend Zoned
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-02-20
* Description  :
* Status       : Accepted (23268603)
* Tags         : java
* Comment      :
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class FRNDZND{
  public static void main(String args[]) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    String[] NQ = br.readLine().split(" ");
    String[] LR;
    int Q = Integer.parseInt(NQ[1]);
    String[] A = br.readLine().split(" ");

    for(int t = 0; t < Q; t++){
      LR = br.readLine().split(" ");

      if (LR[0].equals(LR[1])){
        System.out.println(A[Integer.parseInt(LR[0]) - 1]);
      } else {
        System.out.println(0);
      }
    }
  }
}
