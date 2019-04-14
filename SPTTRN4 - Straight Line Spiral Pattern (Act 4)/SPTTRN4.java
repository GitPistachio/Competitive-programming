/*
* Project name : SPOJ: SPTTRN4 - Straight Line Spiral Pattern (Act 4)
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-04-12
* Description  :
* Status       : Accepted (23624530)
* Tags         : java, console pattern
* Comment      :
*/

import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.lang.StringBuilder;

final class SPTTRN4{
    static class Reader{
      final private int BUFFER_SIZE = 1 << 16;
      private DataInputStream din;
      private byte[] buffer;
      private int bufferPointer, bytesRead;

      public Reader()
      {
          din = new DataInputStream(System.in);
          buffer = new byte[BUFFER_SIZE];
          bufferPointer = bytesRead = 0;
      }

      public Reader(String file_name) throws IOException
      {
          din = new DataInputStream(new FileInputStream(file_name));
          buffer = new byte[BUFFER_SIZE];
          bufferPointer = bytesRead = 0;
      }

      public int nextInt() throws IOException
      {
          int ret = 0;
          byte c = read();
          while (c <= ' ')
              c = read();
          boolean neg = (c == '-');
          if (neg)
              c = read();
          do
          {
              ret = ret * 10 + c - '0';
          }  while ((c = read()) >= '0' && c <= '9');

          if (neg)
              return -ret;
          return ret;
      }

      private void fillBuffer() throws IOException
      {
          bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
          if (bytesRead == -1)
              buffer[0] = -1;
      }

      private byte read() throws IOException
      {
          if (bufferPointer == bytesRead)
              fillBuffer();
          return buffer[bufferPointer++];
      }

      public void close() throws IOException
      {
          if (din == null)
              return;
          din.close();
      }
  }

  public static int min(int x, int y){
    if (x < y){
        return x;
    } else {
        return y;
    }
  }

  public static String drawMaizeTile(int s, int ith, int jth){
    int m = min(min(s - ith - 1, s - jth - 1), min(ith, jth));

    if (m > 1){
        int k = 2*(m/2);
        return drawMaizeTile(s - 2*k, ith - k, jth - k);
    }

    if (s == 1) return "*\n";
    if (s == 2){
        if (ith == 0 && jth == 1)
            return ".\n";
        else
            return "*\n";
    }

    if ((ith == 0 || jth == 0 || s == ith + 1 || s == jth + 1) && (ith != 0 || jth != 1)){
        return "*\n";
    } else {
        if (s >= 5 && ith == 1 && jth == 2){
            return "*\n";
        } else {
            return ".\n";
        }
    }
  }
  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();

    int n, ith, jth, T = r.nextInt();

    for (int t = 0; t < T; t++){
      n = r.nextInt();
      ith = r.nextInt() - 1;
      jth = r.nextInt() - 1;
      sb.append(drawMaizeTile(n, ith, jth));
    }
    System.out.print(sb.toString());
  }
}
