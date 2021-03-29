/*
* Project name : SPOJ: FIB64 - 64bit-Fibonacci
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-02-16
* Description  :
* Status       : Accepted (23242792)
* Tags         : java, fibonacci sequence, integer sequence a000045 (oeis)
* Comment      : 3000
*/

import java.util.Scanner;

class FIB64S3{
  static long modMul(long a, long b, long m){
    if (a < Integer.MAX_VALUE && b < Integer.MAX_VALUE){
      return (a * b) % m;
    }

    long result = 0;
    a = a % m;
    while (b > 0){
      if (b % 2 == 1){
        result = (result + a) % m;
      }
      a = (a << 1) % m;

      b = b >> 1;
    }

    return result % m;
  }

  public static void moduloFibonacci(long n, long m, long F[]){
    if (n > 2){
      long[] Fa = new long[3];
      long f11, f12;

      moduloFibonacci(n/2, m, Fa);

      f11 = modMul(Fa[1], Fa[1], m);
      f12 = modMul(Fa[1], Fa[2], m);

      F[2] = f11 + modMul(Fa[2], Fa[2], m);
      F[1] = f11 + 2*f12;
      F[0] = F[1] + F[2];

      if (n % 2 == 1){
        F[2] = F[1];
        F[1] = F[0];
        F[0] = F[1] + F[2];
      }
    } else if (n == 2){
      F[0] = 2;
      F[1] = 1;
      F[2] = 1;
    } else{
      F[0] = 1;
      F[1] = 1;
      F[2] = 0;
    }
  }

  public static void moduloFibonacci(long n, int m, int F[]){
    if (n > 2){
      int[] Fa = new int[3];
      int f11, f12;
      moduloFibonacci(n/2, m, Fa);

      f11 = (Fa[1]*Fa[1]) % m;
      f12 = (Fa[1]*Fa[2]) % m;

      F[2] = f11 + (Fa[2]*Fa[2]) % m;
      F[1] = f11 + 2*f12;
      F[0] = F[1] + F[2];

      if (n % 2 == 1){
        F[2] = F[1];
        F[1] = F[0];
        F[0] = F[1] + F[2];
      }
    } else if (n == 2){
      F[0] = 2;
      F[1] = 1;
      F[2] = 1;
    } else{
      F[0] = 1;
      F[1] = 1;
      F[2] = 0;
    }
  }

  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    long n, m;
    long[] lF = new long[3];
    int[] iF = new int[3];

    for (int i=0; i < 3000; i++){
      n = sc.nextLong();
      m = sc.nextLong();

      if (n > 1){
        if (m < Integer.MAX_VALUE){
          moduloFibonacci(n - 1, (int)m, iF);
          System.out.println(iF[0] % m);
        }
        else{
          moduloFibonacci(n - 1, m, lF);
          System.out.println(lF[0] % m);
        }
      } else{
        System.out.println(0);
      }
    }
  }
}
