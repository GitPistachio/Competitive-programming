/*
* Project name : SPOJ: CEQU - Crucial Equation
* Author       : Wojciech Raszka
* Date created : 2019-03-30
* Description  :
* Status       : Accepted (23531267)
* Tags         : java, fast I/O, Bézout's identity, gcd, greatest common divisor
* Comment      :
*/

import java.io.DataInputStream;
import java.io.IOException;

final class CEQU{
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

  public static int gcd(int a, int b){
    if (b == 0){
      return a;
    } else {
      return gcd(b, a % b);
    }
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();

    int T = r.nextUnsignedInt();
    int a, b, c;

    for (int t = 1; t <= T; t++){
      a = r.nextUnsignedInt();
      b = r.nextUnsignedInt();
      c = r.nextUnsignedInt();
      sb.append("Case ");
      sb.append(t);
      if (c % gcd(a, b) == 0){
        sb.append(": Yes\n");
      } else {
        sb.append(": No\n");
      }
    }
    System.out.print(sb.toString());
  }
}
