/*
* Project name : SPOJ: ICANDIES - Candies
* Author       : Wojciech Raszka
* Date created : 2019-03-09
* Description  :
* Status       : Accepted (23373828)
* Comment      :
*/


import java.util.Scanner;

class ICANDIES{
  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);

    int T = sc.nextInt();
    int i, n;

    for (int t = 0; t < T; t++){
      n = sc.nextInt();
      for (i = 5; i < n - 3; i+=5){
        if ((n - i) % 3 == 0) break;
      }
      if (n - i >= 3 && (n - i) % 3  == 0){
        System.out.println("Case " + (t + 1) + ": " + (n - i));
      } else {
        System.out.println("Case " + (t + 1) + ": -1");
      }
    }
  }
}
