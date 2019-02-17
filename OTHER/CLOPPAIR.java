/*
* Project name : SPOJ: Closest point problem
* Author       : Wojciech Raszka
* Date created : 2019-02-09
* Description  :
* Status       : Time limit exceeded
* Comment      : O(N^2)
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
	Arrays.sort(points);

    long dx, dy, h = Long.MAX_VALUE;
    int a = 0, b = 0;

    for (int i=0; i < n - 1; i++){
        for (int j=i+1; j < n; j++){
          if (points[j].x - points[i].x > h){
            break;
          }
          dx = ((long)points[i].x - points[j].x)*((long)points[i].x - points[j].x);
          dy = ((long)points[i].y - points[j].y)*((long)points[i].y - points[j].y);
          if (dx + dy < h){
            a = points[i].idx;
            b = points[j].idx;
            h = dx + dy;
          }
        }
    }
    if (a > b){
      int t = b;
      b = a;
      a = t;
    }
    System.out.printf(a + " " + b + " %.6f", Math.sqrt(h));
  }
}
