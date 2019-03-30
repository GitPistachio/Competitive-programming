/*
* Project name : SPOJ: RPLE - Espionage
* Author       : Wojciech Raszka
* Date created : 2019-03-18
* Description  :
* Status       : Accepted (23441230)
* Comment      :
*/

import java.io.DataInputStream;
import java.io.IOException;

final class RPLE{
  static class Reader{
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
    boolean[][] spy;
    int N, R, R1, R2;
    boolean is_spy_spying_spy;

    for (int t = 1; t <= T; t++){
      N = r.nextUnsignedInt();
      R = r.nextUnsignedInt();
      spy = new boolean[N][2];
      is_spy_spying_spy = false;
      while (R-- > 0){
        R1 = r.nextUnsignedInt();
        R2 = r.nextUnsignedInt();

        if (spy[R2][0]){
          is_spy_spying_spy = true;
          r.omitLines(R);
          break;
        } else {
          spy[R2][1] = true;
        }

        if (spy[R1][1]){
          is_spy_spying_spy = true;
          r.omitLines(R);
          break;
        } else {
          spy[R1][0] = true;
        }
      }
      if (is_spy_spying_spy){
        System.out.println("Scenario #" + t + ": spied");
      } else {
        System.out.println("Scenario #" + t + ": spying");
      }
    }
  }
}
