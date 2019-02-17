/*
* Project name : SPOJ: Friends of Friends
* Author       : Wojciech Raszka
* Date created : 2019-02-07
* Description  :
* Status       : Accepted (23191581)
* Comment      :
*/

import java.util.Scanner;
import java.util.Set;
import java.util.HashSet;

class  FACEFRND{
  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);

    int N, M;
    Set<Integer> fofs = new HashSet<Integer>();
    Set<Integer> fs = new HashSet<Integer>();
    N = sc.nextInt();

    for (int i=0; i < N; i++){
      fs.add(sc.nextInt());
      M = sc.nextInt();
      for (int j=0; j < M; j++){
        fofs.add(sc.nextInt());
      }
    }
    fofs.removeAll(fs);
    System.out.println(fofs.size());
  }
}
