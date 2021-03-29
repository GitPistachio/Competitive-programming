/*
* Project name : SPOJ: HANGOVER - Hangover
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2019-04-02
* Description  :
* Status       : Accepted (23554826)
* Tags         : java, fast I/O, math, harmonic series, block-stacking problem, dynamic programming, DP
* Comment      :
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;
import java.lang.Math;

final class HANGOVER{
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

      public double nextDouble() throws IOException{
            double ret = 0, div = 1;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();

            do {
                ret = ret * 10 + c - '0';
            }
            while ((c = read()) >= '0' && c <= '9');

            if (c == '.'){
                while ((c = read()) >= '0' && c <= '9'){
                    ret += (c - '0') / (div *= 10);
                }
            }

            if (neg)
                return -ret;
            return ret;
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
  public static double abs(double x){
    if (x < 0)
      return -x;
    else
      return x;
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    int[] H = new int[521];
    double h = 0;
    int l, k = 0;

    for (int i = 2; h <= 5.2; i++){
      h += 1.0/i;
      while ( k <= (int) (100*h)){
        H[k++] = i - 1;
      }
      //System.out.println((i - 1) + " " + (k - 1) + " " + (int) (100*h) + " " + h);
    }
    while ((l = (int) Math.round(100*r.nextDouble())) != 0){
      sb.append(H[l]);
      sb.append(" card(s)\n");
    }
    System.out.print(sb.toString());
  }
}
