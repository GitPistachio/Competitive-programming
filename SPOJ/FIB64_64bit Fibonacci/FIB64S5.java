/*
* Project name : SPOJ: FIB64 - 64bit Fibonacci
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-02-10
* Description  :
* Status       : Accepted (23204186)
* Tags         : java, math, fibonacci sequence, integer sequence a000045 (oeis)
* Comment      : 5000
*/

import java.util.Scanner;
import java.lang.Math;
import java.math.BigInteger;

class FIB64S5{
  public static void moduloFibonacci(long n, BigInteger m, BigInteger F[]){
    if (n > 2){
      BigInteger[] Fa = new BigInteger[3];

      moduloFibonacci(n/2, m, Fa);

      F[0] = Fa[0].multiply(Fa[0]).add(Fa[1].multiply(Fa[1])).mod(m);
      F[1] = Fa[0].multiply(Fa[1]).add(Fa[1].multiply(Fa[2])).mod(m);
      F[2] = Fa[1].multiply(Fa[1]).add(Fa[2].multiply(Fa[2])).mod(m);

      if (n % 2 == 1){
        F[2] = F[1];
        F[1] = F[0];
        F[0] = F[1].add(F[2]).mod(m);
      }
    } else if (n == 2){
      F[0] = BigInteger.valueOf(2);
      F[1] = BigInteger.valueOf(1);
      F[2] = BigInteger.valueOf(1);
    } else{
      F[0] = BigInteger.valueOf(1);
      F[1] = BigInteger.valueOf(1);
      F[2] = BigInteger.valueOf(0);
    }
  }

  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    long n;
    BigInteger[] F = new BigInteger[3];
    BigInteger m;

    for (int i=0; i < 5000; i++){
      n = sc.nextLong();
      m = BigInteger.valueOf(sc.nextLong());

      if (n > 1){
        moduloFibonacci(n - 1, m, F);
        System.out.println(F[0]);
      } else{
        System.out.println(0);
      }
    }
  }
}
