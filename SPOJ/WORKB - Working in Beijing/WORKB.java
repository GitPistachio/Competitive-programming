/*
* Project name : SPOJ: WORKB - Working in Beijing
* Author       : Wojciech Raszka
* Date created : 2019-03-20
* Description  :
* Status       : Accepted (23456172)
* Tags         : java, fast I/O, sliding window technique
* Comment      :
*/

import java.io.DataInputStream;
import java.io.IOException;

class WORKB{
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
    long n, a, b;
    long min_cost;
    long t1, t2;

    for (int t = 1; t <= T; t++){
      n = r.nextUnsignedInt();
      a = r.nextUnsignedInt();
      b = r.nextUnsignedInt();

      min_cost = 2*a + b;
      t1 = r.nextUnsignedInt();
      while (n-- > 1){
        t2 = r.nextUnsignedInt();
        if ((t2 - t1 - 1)*b <= 2*a){
          min_cost += (t2 - t1)*b;
        } else {
          min_cost += 2*a + b;
        }
        t1 = t2;
      }

      System.out.println("Case #" + t + ": " + min_cost);
    }
  }
}
