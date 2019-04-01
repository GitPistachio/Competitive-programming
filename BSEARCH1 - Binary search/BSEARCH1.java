/*
* Project name : SPOJ: BSEARCH1 - Binary search
* Author       : Wojciech Raszka
* Date created : 2019-04-01
* Description  :
* Status       : Accepted (23544532)
* Tags         : java, fast I/O, leftmost binary search
* Comment      :
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;

final class BSEARCH1{
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

  public static int findIdx(int x, int n, int A[]){
    int m, l = 0, r = n;

    while (l < r){
        m = (l + r)/2;
        if (A[m] < x){
          l = m + 1;
        } else {
          r = m;
        }
    }
    if (l >= n || A[l] != x){
        return -1;
    } else {
      return l;
    }
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();

    int x, n = r.nextUnsignedInt(), q = r.nextUnsignedInt();

    int[] A = new int[n];
    for (int i = 0; i < n; i++){
      A[i] = r.nextInt();
    }
    while (q-- > 0){
      x = r.nextInt();
      sb.append(findIdx(x, n, A));
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
