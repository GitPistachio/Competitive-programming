/*
* Project name : SPOJ: Closest point problem
* Author       : Wojciech Raszka
* Date created : 2019-02-09
* Description  :
* Status       : Time limit exceeded
* Comment      :
*/
import java.util.Scanner;
import java.util.Arrays;
import java.lang.Math;

class Point implements Comparable<Point>{
  public int x;
  public int y;
  public int idx;
  public boolean box;

  public Point(int idx, int x, int y){
    this.x = x;
    this.y = y;
    this.idx = idx;
    this.box = true;
  }

  public int compareTo(Point p){
    return this.x - p.x;
  }
}

class CLOPPAIR{
  public static void main(String args[]){
    Scanner sc = new Scanner(System.in);
    int n = sc.nextInt();
    int x, y;
    Point[] points = new Point[n];

    for (int i=0; i < n; i++){
      x = sc.nextInt();
      y = sc.nextInt();
      points[i] = new Point(i, x, y);
    }

    long d, h = Long.MAX_VALUE;
    int a = 0, b = 0;
    int j = 0;
    for (int i=1; i < n; i++){
      while (j < i && points[i].x - points[j].x > h){
        points[j].box = false;
        j++;
      }

      for (int k=j; k < i; k++){
        if (points[k].box && Math.abs(points[k].y - points[i].y) < h){
          d = ((long)points[k].x - points[i].x)*(points[k].x - points[i].x) + ((long)points[k].y - points[i].y)*(points[k].y - points[i].y);
          if (d < h){
            h = d;
            a = points[i].idx;
            b = points[k].idx;
          }
        }
      }
    }
    if (a > b){
      int t = b;
      b = a;
      a = t;
    }
    System.out.printf(a + " " + b + " %.6f", Math.round(1000000*Math.sqrt(h))/1000000.0);
  }
}
