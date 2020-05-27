/*
* Project name : SPOJ: PR003004 - Digit Sum
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-16
* Description  :
* Status       : Accepted (23926709)
* Tags         : java, sum of digits from 1 to n, integer sequence A037123 (OEIS)
* Comment      :
*/

import java.util.Scanner;

final class PR003004{
  public static long sumOfDigitsFrom1ToN(long n){
    if (n < 10){
      return n*(n + 1) >> 1;
    }

    long msd = n;
    long no_of_digits = 0, p = 1;

    while (msd >= 10){
      no_of_digits++;
      p *= 10;
      msd /= 10;
    }

    return (msd*45*no_of_digits*p/10)+(msd*(msd-1)*p/2)+ msd*(n % p + 1) + sumOfDigitsFrom1ToN(n % p);
  }

  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);

    int T = sc.nextInt();
    long a, b, x;

    while (T-- > 0){
      a = sc.nextLong();
      b = sc.nextLong();

      x = sumOfDigitsFrom1ToN(b) - sumOfDigitsFrom1ToN(a - 1);
      System.out.println(x);
    }
  }
}
