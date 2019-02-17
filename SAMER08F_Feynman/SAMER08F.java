/*
* Project name : SPOJ: Feynman
* Author       : Wojciech Raszka
* Date created : 2019-02-10
* Description  :
* Status       : Accepted (23206019)
* Comment      : It's sum of squares
*/

import java.util.Scanner;

class SAMER08F{
  public static int noOfSquares(int n){
    int no_of_squares = 1;
    for (int i=2; i <= n; i++){
      no_of_squares += i*i;
    }
    return no_of_squares;
  }

  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();

    while (n != 0){
      System.out.println(noOfSquares(n));
      n = sc.nextInt();
    }
  }
}
