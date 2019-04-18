/*
* Project name : SPOJ: CIRCLEDIV - Euler Puzzle
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-04-12
* Description  :
* Status       : Accepted (23634507)
* Tags         : java, fast I/O, math, circle, geometry, integer sequence A000127 (OEIS)
* Comment      : a(n) = 1 + n + n*(n-1)/2 + n*(n-1)*(n - 2)/6 + n*(n-1)*(n - 2)*(n - 3)/24 (5 first elements of nth row of Pascal triangle)
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;

final class CIRCLEDIV{
  static final class Reader{
      final private int BUFFER_SIZE = 1 << 16;
      private DataInputStream dis;
      private byte[] buffer;
      private int bufferPointer, bytesRead;

      public Reader(){
          dis = new DataInputStream(System.in);
          buffer = new byte[BUFFER_SIZE];
          bufferPointer = bytesRead = 0;
      }

      public void omitLines(int n) throws IOException{
        while (n > 0){
          if (read() == '\n')
            n--;
        }
      }

      public double nextDouble() throws IOException{
        double ret = 0, div = 1;
        byte c = read();
        while (c <= ' ')
            c = read();
        boolean neg = (c == '-');
        if (neg)
            c = read();

        do {
            ret = ret * 10 + c - '0';
        }
        while ((c = read()) >= '0' && c <= '9');

        if (c == '.'){
            while ((c = read()) >= '0' && c <= '9'){
                ret += (c - '0') / (div *= 10);
            }
        }

        if (neg)
            return -ret;
        return ret;
      }

      public int nextInt() throws IOException{
          int ret = 0;
          byte c = read();
          while (c <= ' ')
              c = read();
          boolean neg = (c == '-');
          if (neg)
              c = read();
          do{
              ret = ret * 10 + c - '0';
          }  while ((c = read()) >= '0' && c <= '9');

          if (neg)
              return -ret;
          return ret;
      }

      public int nextUnsignedInt() throws IOException{
          int ret = 0;
          byte c = read();
          while (c <= ' ')
              c = read();
          do{
              ret = ret * 10 + c - '0';
          }  while ((c = read()) >= '0' && c <= '9');

          return ret;
      }

      private void fillBuffer() throws IOException{
          bytesRead = dis.read(buffer, bufferPointer = 0, BUFFER_SIZE);
          if (bytesRead == -1)
              buffer[0] = -1;
      }

      private byte read() throws IOException{
          if (bufferPointer == bytesRead)
              fillBuffer();
          return buffer[bufferPointer++];
      }

      public void close() throws IOException{
          if (dis == null)
              return;
          dis.close();
      }
    }

  public static double abs(double x){
    if (x < 0)
      return -x;
    else
      return x;
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();

    int T = r.nextUnsignedInt();
    long n;
    long max_no_of_regions;
    long fifth;
    final long p = 1000000007;

    for (int t = 1; t <= T; t++){
      n = r.nextUnsignedInt() - 1;
      //some weird things because of overflow of long
      fifth = n*(n - 1)*(n - 2)/6;
      if ((fifth & 1) == 0){
        if ((fifth & 2) == 0){
          fifth = (fifth/4)*(n - 3);
        } else {
          fifth = (fifth/2)*((n - 3)/2);
        }
      } else {
        fifth *= (n - 3)/4;
      }
      max_no_of_regions = (1 + n + n*(n - 1)/2 + n*(n - 1)*(n - 2)/6 + fifth) % p;

      sb.append("Case ");
      sb.append(t);
      sb.append(": ");
      sb.append(max_no_of_regions);
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
