/*
* Project name : SPOJ: The Mirror of Galadriel
* Author       : Wojciech Raszka
* Date created : 2019-02-06
* Description  :
* Status       : Accepted (23186506)
* Comment      : The whole string it is own substring thus the string must be a palindrome and that is enough to meet requirements.
*/

import java.util.Scanner;

class AMR12D{
  public static boolean isPalindrome(String str){
    boolean is_palindrome = true;

    for (short i=0, j = (short)(str.length() - 1); i < j; i++, j--){
        if (str.charAt(i) != str.charAt(j)){
            is_palindrome = false;
            break;
        }
    }

    return is_palindrome;
  }
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    short T = sc.nextShort();
    sc.nextLine();

    for (short i=0; i < T; i++){
      if (isPalindrome(sc.nextLine()))
        System.out.println("YES");
      else
        System.out.println("NO");
    }
  }
}
