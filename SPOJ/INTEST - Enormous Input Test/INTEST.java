/*
* Project name : SPOJ: INTEST - Enormous Input Test
* Author       : Wojciech Raszka
* Date created : 2019-03-15
* Description  :
* Status       : Accepted (23415190)
* Comment      : Min 0.18s (23415240)
*/

import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;


class INTEST{
  static class Reader{
      final private int BUFFER_SIZE = 1 << 6;
      private DataInputStream dis;
      private byte[] buffer;
      private int bufferPointer, bytesRead;

      public Reader(){
          dis = new DataInputStream(System.in);
          buffer = new byte[BUFFER_SIZE];
          bufferPointer = bytesRead = 0;
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

    int n = r.nextUnsignedInt(), k = r.nextUnsignedInt();
    int no_of_divisible_int = 0;

    while (n-- > 0){
      if (r.nextUnsignedInt() % k == 0){
        no_of_divisible_int++;
      }
    }
    System.out.println(no_of_divisible_int);
  }
}
