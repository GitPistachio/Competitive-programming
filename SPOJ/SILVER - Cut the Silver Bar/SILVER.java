/*
* Project name : SPOJ: SILVER - Cut the Silver Bar
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-04-14
* Description  :
* Status       : Accepted (23631816)
* Tags         : java, integer sequence A000523 (OEIS), floor logarithm base 2
* Comment      :
*/

import java.util.Scanner;

final class SILVER{
  public static int floorLog2(int n){
    if(n <= 0) throw new IllegalArgumentException();
    return 31 - Integer.numberOfLeadingZeros(n);
  }

  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int n;

    while ((n = sc.nextInt()) != 0){
      System.out.println(floorLog2(n));
    }
  }
}
