/*
* Project name : SPOJ: SEQAGAIN - Easy Sequence!
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-05-14
* Description  :
* Status       : Accepted (23764591)
* Tags         : java, fast I/O, modulo power, modular exponentiation, Fermat's little theorem, math, modulo arithmetic
* Comment      : F(n) = (F(0)^k1)*(F(0)^k2), where k1, k2 could be calculated via matrix (k, k, 1, 0) exponentiation. Because k1, k2 could be large we use Fermat's theorem thus a^k1 mod p = a^K1 mod p, where K1 = k1 mod (p - 1)
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;

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

final class SEQAGAIN{
  public static long power(long x, long y, long p){
    long result = 1;
    x = x % p;
    while (y > 0){
      if (y % 2 == 1){
        result = (result * x) % p;
      }

      y = y >> 1;
      x = (x * x) % p;
    }

    return result;
  }

  public static long [][] matrixPower(long I[][], long n, long p){
    long [][] T;

    if (n > 1){

      T = matrixPower(I, n/2, p);

      long a, b, c, d;
      a = T[0][0]; b = T[0][1];
      c = T[1][0]; d = T[1][1];
      T[0][0] = (a*a + b*c) % (p - 1); T[0][1] = (a*b + b*d) % (p - 1);
      T[1][0] = (c*a + d*c) % (p - 1); T[1][1] = (c*b + d*d) % (p - 1);

      if (n % 2 == 1){
        a = T[0][0]; b = T[0][1];
        c = T[1][0]; d = T[1][1];
        T[0][0] = (a*I[0][0] + b*I[1][0]) % (p - 1); T[0][1] = (a*I[0][1] + b*I[1][1]) % (p - 1);
        T[1][0] = (c*I[0][0] + d*I[1][0]) % (p - 1); T[1][1] = (c*I[0][1] + d*I[1][1]) % (p - 1);

      }

    } else {
      T = new long [2][2];
      T[0][0] = I[0][0]; T[0][1] = I[0][1];
      T[1][0] = I[1][0]; T[1][1] = I[1][1];
    }

    return T;
  }

  public static long f(long n, long k, long a, long b, long p){
    if (n == 0){
      return a;
    } else if (n == 1){
      return b;
    }
    long [][] I = new long[2][2];
    long [][] A;
    I[0][0] = k; I[0][1] = k;
    I[1][0] = 1; I[1][1] = 0;

    A = matrixPower(I, n - 1, p);

    return (power(b, A[0][0], p)*power(a, A[0][1], p)) % p;
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    int T = r.nextPositiveInt();
    long n, k, a, b;
    long p = 1000000007;

    while (T-- > 0){
      a = r.nextPositiveLong();
      b = r.nextPositiveLong();
      n = r.nextPositiveLong();
      k = r.nextPositiveLong();

      sb.append(f(n, k, a, b, p));
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
