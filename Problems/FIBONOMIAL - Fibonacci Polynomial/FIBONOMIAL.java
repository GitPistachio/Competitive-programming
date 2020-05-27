/*
* Project name : SPOJ: FIBONOMIAL - Fibonacci Polynomial
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-13
* Description  : D(n, x) = (x*X + x - 1)/(F(n + 1)x^(n + 1) + F(n)x^(n + 2))
* Status       : Accepted (23915058)
* Tags         : java, fast I/O, fibonacci sequence A000045 (OEIS), fibonacci generating function
* Comment      :
*/


import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;
import java.lang.Math;

final class Reader{
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

  public long nextPositiveLong() throws IOException{
      long ret = 0;
      byte c = read();
      while (c <= ' ')
          c = read();
      do{
          ret = ret * 10 + c - '0';
      }  while ((c = read()) >= '0' && c <= '9');

      return ret;
  }

  public int nextPositiveInt() throws IOException{
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

final class FIBONOMIAL{
  public static long moduloPower(long x, long y, long p){
    if (y == 0){
      return 1;
    }

    long r = moduloPower(x, y >> 1, p) % p;
    r = (r*r) % p;

    if (y % 2 == 0){
      return r;
    } else {
      return (x*r) % p;
    }
  }

  public static long [][] fibonacciMatrixPower(long n, long p){
    long[][] T;

    if (n > 1){

      T = fibonacciMatrixPower(n/2, p);

      long a, b, c, d;
      a = T[0][0]; b = T[0][1];
      c = T[1][0]; d = T[1][1];
      T[0][0] = (a*a + b*c) % p; T[0][1] = (a*b + b*d) % p;
      T[1][0] = (c*a + d*c) % p; T[1][1] = (c*b + d*d) % p;

      if (n % 2 == 1){
        a = T[0][0]; b = T[0][1];
        c = T[1][0]; d = T[1][1];
        T[0][0] = (a + b) % p; T[0][1] = a;
        T[1][0] = (c + d) % p; T[1][1] = c;

      }

    } else {
      T = new long [2][2];
      T[0][0] = 1; T[0][1] = 1;
      T[1][0] = 1; T[1][1] = 0;
    }

    return T;
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    int T = r.nextPositiveInt();
    long n, x, p = 1000000007, a, b, ib, res;
    long[][] F;

    while (T-- > 0){
      n = r.nextPositiveLong();
      x = r.nextPositiveLong() % p;

      if (x > 0 && n > 0){
        b = (x*x + x - 1) % p;
        ib = moduloPower(b, p - 2, p);
        F = fibonacciMatrixPower(n, p);
        a = F[0][0]*moduloPower(x, n + 1, p) + F[0][1]*moduloPower(x, n + 2, p) - x;
        res = ((a % p) * ib) % p;

        if (res < 0){
          res += p;
        }
      } else {
        res = 0;
      }

	    sb.append(res);
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
