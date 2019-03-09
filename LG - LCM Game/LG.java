/*
* Project name : SPOJ: LG - LCM Game
* Author       : Wojciech Raszka
* Date created : 2019-02-23
* Description  :
* Status       : Accepted (23286893)
* Comment      :
*/

import java.util.Scanner;

class LG{
  public static long gcd(long a, long b){
    long r = 0;
    do {
      r = a % b;
      a = b;
      b = r;
    } while (b != 0);
    return a;
  }
  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int n;
    long x, lcm;

    while (sc.hasNextInt()){
      n = sc.nextInt();
      lcm = sc.nextLong();
      for (int i = 1; i < n; i++){
        x = sc.nextLong();
        lcm = lcm*x/gcd(lcm, x);
      }
      System.out.println(lcm);
    }
  }
}
