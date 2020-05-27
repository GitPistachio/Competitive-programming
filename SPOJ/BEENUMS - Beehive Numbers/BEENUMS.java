/*
* Project name : SPOJ: BEENUMS - Beehive Numbers
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-18
* Description  : a(n) = 3*n*(n + 1) + 1
* Status       : Accepted (23939070)
* Tags         : java, fast I/O, perfect square, hex numbers A003215 (OEIS)
* Comment      :
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;
import java.lang.Math;

final class Reader{
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

  public long nextPositiveLong() throws IOException{
      long ret = 0;
      byte c = read();
      while (c <= ' ')
          c = read();
      do{
          ret = ret * 10 + c - '0';
      }  while ((c = read()) >= '0' && c <= '9');

      return ret;
  }

  public int nextPositiveInt() throws IOException{
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

final class BEENUMS{
  public static boolean isPerfectSquare(double x){
    double squre_root_x = Math.sqrt(x);

    return (squre_root_x*squre_root_x == x);
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    long x, delta;

    while ((x = r.nextInt()) != -1) {
      if (x > 6) {
          delta = Math.round(Math.sqrt(12*x - 3));
          if (delta*delta == 12*x - 3) {
            if ((delta - 3) % 6 == 0) {
              sb.append("Y\n");
            } else {
              sb.append("N\n");
            }
          } else {
            sb.append("N\n");
          }
      } else if (x == 1) {
        sb.append("Y\n");
      } else {
        sb.append("N\n");
      }
    }

    System.out.print(sb.toString());
  }
}
