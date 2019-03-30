/*
* Project name : SPOJ: BUYINT - Buying Integers
* Author       : Wojciech Raszka
* Date created : 2019-03-24
* Description  :
* Status       : Accepted (23482546)
* Tags         : java, fast I/O, math
* Comment      : Dmin = |x*(x - 1) + (n - x)*(n - x - 1) + x*(n - x)|, where x = round((n + sqrt(n))/2)
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;
import java.lang.Math;

final class BUYINT{
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

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();

    int T = r.nextUnsignedInt();
    long n, x, y, Dmin;
    for (int t = 1; t <= T; t++){
      n = r.nextUnsignedInt();
      x = Math.round((n + Math.sqrt(n))/2.0);
      y = n - x;
      Dmin = x*(x - 1)/2 + y*(y - 1)/2 - x*y;
      if (Dmin < 0){
        Dmin = -Dmin;
      }
      sb.append("Case ");
      sb.append(t);
      sb.append(": ");
      sb.append(Dmin);
      sb.append('\n');
    }

    System.out.print(sb.toString());
  }
}
