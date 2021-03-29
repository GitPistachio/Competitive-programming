/*
* Project name : SPOJ: MARBLES - Marbles
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2019-04-18
* Description  :
* Status       : Accepted (23651369)
* Tags         : java, gcd, greatest common divisor, combinations without repetition, math, combinatorics
* Comment      :
*/

import java.io.DataInputStream;
import java.io.IOException;

final class MARBLES{
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

  public static long gcd(long a, long b){
    if (b == 0) return a;

    return gcd(b, a % b);
  }

  public static long combination(long n, long k){
    if (k > n - k) k = n - k;

    long no_of_possibilities = 1;
    long d;
    for (long i = 0; i < k; i++){
        d = gcd(n - i, i + 1);
        no_of_possibilities = ((n - i)/d)*(no_of_possibilities/((i + 1)/d));
    }

    return no_of_possibilities;
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();

    int T = r.nextUnsignedInt(), n, k;

    while (T-- > 0){
      n = r.nextUnsignedInt() - 1;
      k = r.nextUnsignedInt() - 1;

      System.out.println(combination(n, k));
    }
  }
}
