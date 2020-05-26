/*
* Project name : SPOJ: INTEST - Enormous Input Test
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-20
* Description  :
* Status       : Accepted (23947308)
* Tags         : java, fast I/O
* Comment      : 0.17s Read whole data at one.
*/

import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;


final class INTEST2{
  static class Reader{
      final private int BUFFER_SIZE = 1 << 25;
      private DataInputStream dis;
      private byte[] buffer;
      private int bufferPointer, bytesRead;

      public Reader() throws IOException{
          dis = new DataInputStream(System.in);
          buffer = new byte[BUFFER_SIZE];
          bufferPointer = bytesRead = 0;
          fillBuffer();
      }

      public int nextNonNegativeInt() throws IOException{
        int ret = 0;
        do{
            ret = ret * 10 + buffer[bufferPointer++] - '0';
        }  while (buffer[bufferPointer] >= '0');
        bufferPointer++;

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

    int n = r.nextNonNegativeInt(), k = r.nextNonNegativeInt();
    int no_of_divisible_int = 0;

    for (int i = 0; i < n; i++){
      if (r.nextNonNegativeInt() % k == 0){
        no_of_divisible_int++;
      }
    }
    System.out.println(no_of_divisible_int);
  }
}
