/*
* Project name : SPOJ: HS12HDPW - Hidden Password
* Author       : Wojciech Raszka
* Date created : 2019-03-11
* Description  :
* Status       : Accepted (23402563)
* Comment      :
*/

import java.util.Scanner;

class HS12HDPW{
  public static byte getBit(char c, int position){
    return (byte) (c >> position & 1);
  }
  public static void fillIdx(int p, char key[], int idx[]){
    StringBuilder a = new StringBuilder("00"), b = new StringBuilder("00");
    for (int i =  5; i >= 0; i--){
      a.append(getBit(key[i], i));
      b.append(getBit(key[i], (i + 3) % 6));
    }
    idx[2*p] = Integer.parseInt(a.toString(), 2);
    idx[2*p + 1] = Integer.parseInt(b.toString(), 2);
  }
  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);

    int T = sc.nextInt();
    int n;

    char[] key = new char[6], val = new char[64];
    int[] idx;
    StringBuilder pwd = new StringBuilder();

    for (int t = 0; t < T; t++){
      n = sc.nextInt();
      idx = new int[2*n];
      for (int i = 0; i < n; i++){
        key = sc.next().toCharArray();
        fillIdx(i, key, idx);
      }
      val = sc.next().toCharArray();

      for (int i = 0; i < 2*n; i++){
        pwd.append(val[idx[i]]);
      }
      System.out.println(pwd.toString());
      pwd.setLength(0);
    }
  }
}
