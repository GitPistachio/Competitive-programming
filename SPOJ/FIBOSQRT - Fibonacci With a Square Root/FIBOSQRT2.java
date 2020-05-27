/*
* Project name : SPOJ: FIBOSQRT - Fibonacci With a Square Root
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-12
* Description  : A(n) = B(n) + x*C(n) for n > 2, where x = A(2) - A(1) - 3*A(0), C(n) = F(n)F(n - 1), B(n) = 2*(B(n - 1) + B(n - 2)) + n, B(0) = A(0), B(1) = A(1), B(2) = A(2)
* Status       : Accepted (23909151)
* Tags         : java, fast I/O, floor sqrt, fibonacci sequence A000045 (OEIS), integer sequence A079472(OEIS), integer sequence A007598 (OEIS), golden rectangle numbers A001654 (OEIS)
* Comment      : It turns out that C(n) is related to golden rectangle numbers which simplify its calculation
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

final class FIBOSQRT2{
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
    long f0, f1, n, p, x, sn, h2, hn, result, a, d, g;
    long[][] F, H;

    while (T-- > 0){
      f0 = r.nextPositiveLong();
      f1 = r.nextPositiveLong();
      p = r.nextPositiveLong();
      n = r.nextPositiveLong();

      if (n > 2){
        x = ((Math.round(Math.sqrt(3 + f1*f0)) - f0) << 1) % p;
        F = fibonacciMatrixPower(n - 1, p);

        sn = (x*((F[0][0]*F[0][1]) % p)) % p;
        a = (F[0][0]*F[0][1]) % p;
        d = (F[0][0]*(F[0][0] - F[0][1])) % p;
        g = (F[0][1]*(F[0][1] - F[0][0])) % p;

        h2 = (f1 + 3*f0) % p;
        hn = (h2*a + f1*d + f0*g) % p;

        result = sn + hn;
      } else if (n == 2) {
        result = f1 + f0 + (Math.round(Math.sqrt(3 + f1*f0)) << 1);
      }  else if (n == 1) {
        result = f1;
      } else {
        result = f0;
      }

      result = result % p;

      if (result < 0){
        result += p;
      }

      sb.append(result);
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
