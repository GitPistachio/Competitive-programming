/*
* Project name : SPOJ: EKO - Eko
* Author       : Wojciech Raszka
* Email        : gitpistachio@gmail.com
* Date created : 2019-04-17
* Description  :
* Status       : Accepted (23649953)
* Tags         : java, fast I/O, discrete binary search
* Comment      :
*/

import java.io.DataInputStream;
import java.io.IOException;

final class EKO{
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

  static int[] A;

  public static boolean p(int h, int n, int M){
    for (int i = 0; i < n; i++){
      if (h < A[i]) M -= A[i] - h;
      if (M <= 0) return true;
    }
    return false;
  }

  public static int binary_search(int l, int r, int n, int M){
    int h;
    while (l < r){
      h = l + (r - l + 1)/2;
      if (p(h, n, M)){
        l = h;
      } else{
        r = h - 1;
      }
    }
    return l;
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();

    int n = r.nextUnsignedInt(), M = r.nextUnsignedInt();
    A = new int[n];

    for(int i = 0; i < n; i++){
      A[i] = r.nextUnsignedInt();
    }

    System.out.println(binary_search(0, 1000000000, n, M));
  }
}
