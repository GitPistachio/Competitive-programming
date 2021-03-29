/*
* Project name : SPOJ: FIBFUNCH - Fun with Fibonacci Series (Challenge)
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2019-06-11
* Description  : A(n) = b*F(n + 2) + a*F(n + 1) - b , where F is Fibonacci sequence
* Status       : Accepted (23906933)
* Tags         : java, fast I/O, fibonacci sequence, integer sequence A000045 (OEIS), partial sum of Fibonacci numbers, integer sequence A000071 (OEIS)
* Comment      : 1729. It could be massivly reduce. I think doublig method here will be more appropriate
*/

import java.util.Scanner;

final class FIBOSUM{
  public static long [][] matrixPower(long I[][], long n, long p){
    long[][] T;

    if (n > 1){

      T = matrixPower(I, n/2, p);

      long a, b, c, d;
      a = T[0][0]; b = T[0][1];
      c = T[1][0]; d = T[1][1];
      T[0][0] = (a*a + b*c) % p; T[0][1] = (a*b + b*d) % p;
      T[1][0] = (c*a + d*c) % p; T[1][1] = (c*b + d*d) % p;

      if (n % 2 == 1){
        a = T[0][0]; b = T[0][1];
        c = T[1][0]; d = T[1][1];
        T[0][0] = (a*I[0][0] + b*I[1][0]) % p; T[0][1] = (a*I[0][1] + b*I[1][1]) % p;
        T[1][0] = (c*I[0][0] + d*I[1][0]) % p; T[1][1] = (c*I[0][1] + d*I[1][1]) % p;

      }

    } else {
      T = new long [2][2];
      T[0][0] = I[0][0]; T[0][1] = I[0][1];
      T[1][0] = I[1][0]; T[1][1] = I[1][1];
    }

    return T;
  }

  public static long fibonacci(long n, long first, long second, long p){
    if (n > 2){
      long[][] T, I = new long [2][2];
      I[0][0] = 1; I[0][1] = 1;
      I[1][0] = 1; I[1][1] = 0;

      T = matrixPower(I, n - 1, p);


      return (second*T[0][0] + first*T[1][0]) % p;
    } else if (n == 2){
      return (second + first) % p;
    } else if (n == 1){
      return second % p;
    }

    return first;
  }

  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    StringBuilder sb = new StringBuilder();
    int first, second, n, T = sc.nextInt();
    long p, result;

    while (T-- > 0){
      first = sc.nextInt();
      second = sc.nextInt();
      n = sc.nextInt();
      p = sc.nextInt();

      result = (fibonacci(n + 1, first, second, p) - (second % p)) % p;
      if (result < 0){
      	result += p;
      }

        System.out.println(result);
    }
  }
}
