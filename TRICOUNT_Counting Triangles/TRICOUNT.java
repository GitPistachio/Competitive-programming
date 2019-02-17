/*
* Project name : SPOJ: Counting triangles
* Author       : Wojciech Raszka
* Date created : 2019-02-12
* Description  :
* Status       : Accepted (23218796)
* Comment      : There is a direct formula n*(n + 2)*(2*n + 1)/8
*/

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

class TRICOUNT{
  public static void main(String args[]) throws IOException{
    BufferedReader r = new BufferedReader(new InputStreamReader(System.in));
    int T = Integer.parseInt(r.readLine());
    long n;

    for (int t=0; t < T; t++){
        n = Long.parseLong(r.readLine());
        System.out.println((long)(n*(n + 2)*(2*n + 1)/8));
    }
  }
}
