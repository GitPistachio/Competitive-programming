/*
* Project name : SPOJ: HCOUPLE - Hidden Couple
* Author       : Wojciech Raszka
* Date created : 2019-02-23
* Description  :
* Status       : Accepted (23286666)
* Comment      :
*/

import java.util.Scanner;

class HCOUPLE{
  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);

    int T = sc.nextInt(); sc.nextLine();
    int name_value;
    char[] name;

    for (int t = 1; t <= T; t++){
      name = sc.nextLine().toCharArray();
      name_value = 0;
      for (int i = 0; i < name.length; i++){
        name_value += name[i];
      }
      if (name_value % 3 == 0){
        System.out.println("Case " + t + ": Yes");
      } else {
        System.out.println("Case " + t + ": No");
      }
    }
  }
}
