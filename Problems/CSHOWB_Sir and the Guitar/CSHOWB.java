/*
* Project name : SPOJ: CSHOWB - Sir and the Guitar
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-03-08
* Description  :
* Status       : Accepted (23367543)
* Tags         ; java, stack
* Comment      :
*/

import java.util.Scanner;
import java.util.Stack;
import java.util.ArrayList;


class CSHOWB{
  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt(), P = sc.nextInt();
    ArrayList<Stack<Integer>> G = new ArrayList<Stack<Integer>>();
    for (int i = 0; i < 6; i++){
      G.add(new Stack<Integer>());
    }
    int s, f;
    int no_of_finger_movements = 0;

    for(int i = 0; i < N; i++){
      s = sc.nextInt() - 1;
      f = sc.nextInt();

      while (!G.get(s).empty()){
        if (G.get(s).peek() <= f){
          break;
        }
        G.get(s).pop();
        no_of_finger_movements++;
      }
      if (G.get(s).empty() || G.get(s).peek() < f){
        G.get(s).push(f);
        no_of_finger_movements++;
      }
    }
    System.out.println(no_of_finger_movements);
  }
}
