/*
* Project name : SPOJ: Simple Arithmetics II
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-02-08
* Description  :
* Status       : Accepted (23195291)
* Tags         : python, math, evaluation of formula
* Comment      :
*/

import java.util.Scanner;

class ARITH2{
  public static long eval(String eq){
    int idx = -1, cidx;
    byte flag = 0;

    cidx = eq.lastIndexOf("*");
    if (cidx >= 0){
      idx = cidx;
      flag = 1;
    }
    cidx = eq.lastIndexOf("/");
    if (cidx > idx){
      idx = cidx;
      flag = 2;
    }
    cidx = eq.lastIndexOf("+");
    if (cidx > idx){
      idx = cidx;
      flag = 3;
    }
    cidx = eq.lastIndexOf("-");
    if (cidx > idx){
      idx = cidx;
      flag = 4;
    }

    if (flag == 1){
      return eval(eq.substring(0, idx)) * eval(eq.substring(idx + 1));
    }
    else if (flag == 2){
      return eval(eq.substring(0, idx)) / eval(eq.substring(idx + 1));
    }
    else if (flag == 3){
      return eval(eq.substring(0, idx)) + eval(eq.substring(idx + 1));
    }
    else if (flag == 4){
      return eval(eq.substring(0, idx)) - eval(eq.substring(idx + 1));
    }

    return Long.valueOf(eq);
  }
  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    long T = sc.nextLong();
    sc.nextLine();

    String eq;
    for (int t=0; t < T; t++){
      sc.nextLine();
      eq = sc.nextLine();
      eq = eq.replaceAll("\\s+", "");
      eq = eq.replace("=", "");
      System.out.println(eval(eq));
    }
  }
}
