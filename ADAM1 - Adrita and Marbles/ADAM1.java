/*
* Project name : SPOJ: ADAM1 - Adrita and Marbles
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-03-21
* Description  :
* Status       : Accepted (23462619)
* Tags         : java, fast I/O, circle, geometry, math
* Comment      : Standard form of circle equation (x - x0)^2 + (y - y0)^2 = r^2
*/

import java.io.DataInputStream;
import java.io.IOException;

class ADAM1{
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
    int T = r.nextUnsignedInt();
    long p, q, z, n, x, y;
    int no_of_fitting_marbles;

    while (T-- > 0){
      p = r.nextUnsignedInt();
      q = r.nextUnsignedInt();
      z = r.nextUnsignedInt();

      n = r.nextUnsignedInt();
      no_of_fitting_marbles = 0;
      while (n-- > 0){
        x = r.nextUnsignedInt();
        y = r.nextUnsignedInt();

        if ((2*x - p)*(2*x - p) + (2*y - q)*(2*y - q) <=  p*p + q*q - 4*z){
            no_of_fitting_marbles++;
        }
      }

      System.out.println(no_of_fitting_marbles);
    }
  }
}
