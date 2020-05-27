/*
* Project name : SPOJ: TTREAT - Happy Telephones
* Author       : Wojciech Raszka
* E-mail       : gitpistachio.gmail.com
* Date created : 2019-03-23
* Description  :
* Status       : Accepted (23479506)
* Tags         : java, fast I/O, overlapping interval
* Comment      : The same problem as HAPPYTL
*/

import java.io.DataInputStream;
import java.io.IOException;

final class TTREAT{
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
    int N, M;
    int[][] phone_calls = new int[10001][2];
    int start, end, no_of_hits;

    N = r.nextUnsignedInt();
    M = r.nextUnsignedInt();
    while (N != 0 && M != 0){
      for (int i = 0; i < N; i++){
        r.nextUnsignedInt();
        r.nextUnsignedInt();
        phone_calls[i][0] = r.nextUnsignedInt();
        phone_calls[i][1] = phone_calls[i][0] + r.nextUnsignedInt();
      }

      for (int i = 0; i < M; i++){
        start = r.nextUnsignedInt();
        end = start + r.nextUnsignedInt();
        no_of_hits = 0;
        for (int c = 0; c < N; c++){
          if (end > phone_calls[c][0] && phone_calls[c][1] > start){
            no_of_hits++;
          }
        }
        System.out.println(no_of_hits);
      }
      N = r.nextUnsignedInt();
      M = r.nextUnsignedInt();
    }
  }
}
