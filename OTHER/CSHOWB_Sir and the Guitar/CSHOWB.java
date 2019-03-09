/*
* Project name : SPOJ: CSHOWB - Sir and the Guitar
* Author       : Wojciech Raszka
* Date created : 2019-03-08
* Description  :
* Status       :
* Comment      :
*/

import java.util.Scanner;
import java.util.SortedSet;
import java.util.TreeSet;
import java.util.ArrayList;


class CSHOWB{
  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt(), P = sc.nextInt();
    ArrayList<SortedSet<Integer>> G = new ArrayList<SortedSet<Integer>>();
    for (int i = 0; i < 6; i++){
      G.add(new TreeSet<>());
    }
    int s, f;
    int no_of_finger_movements = 0;

    for(int i = 0; i < N; i++){
      s = sc.nextInt() - 1;
      f = sc.nextInt();

      if (G.get(s).isEmpty()){
        G.get(s).add(f);
        no_of_finger_movements++;
      } else if (G.get(s).last() < f){
        G.get(s).add(f);
        no_of_finger_movements++;
      } else {
        no_of_finger_movements += G.get(s).tailSet(f).size();
        SortedSet<Integer> Shead = new TreeSet<>();
        Shead.addAll(G.get(s).headSet(f));
        if (G.get(s).contains(f)){
          G.set(s, Shead);
        } else {
          G.set(s, Shead);
          G.get(s).add(f);
          no_of_finger_movements++;
        }
      }
    }
    System.out.println(no_of_finger_movements);
  }
}
