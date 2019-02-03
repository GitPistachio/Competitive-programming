//Solution of 24th problem in SPOJ called Small factorials

import java.util.Scanner;
import java.math.BigInteger;

class FCTRL2
{
  public static BigInteger factorial(int n)
  {
    if (n > 1)
      return factorial(n - 1).multiply(BigInteger.valueOf(n));

    return BigInteger.valueOf(1);
  }
  public static void main(String[] args)
  {
    Scanner sc = new Scanner(System.in);
    int no_of_test_cases;

    no_of_test_cases  = sc.nextInt();

    for (int i=1; i<=no_of_test_cases; i++)
    {
      System.out.println(factorial(sc.nextInt()));
    }
  }
}
