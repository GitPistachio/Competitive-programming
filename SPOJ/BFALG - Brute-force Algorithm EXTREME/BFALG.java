/*
* Project name : SPOJ: BFALG - Brute-force Algorithm EXTREME
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2019-05-15
* Description  :
* Status       : Accepted (23769087)
* Tags         : java, fast I/O, fast modular matrix exponentiation, Fermat's little theorem, math, modular arithmetic, Euler's theorem, Euler's totient funcion, fibonacci sequence, integer sequence a000045 (oeis)
* Comment      : Similar to SEQAGAIN for k = 1 (this matrix form is used to calculate Fibonacci sequence). You have to applay generalization of Euler's theorem for any integers not only coprimes.
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

final class BFALG{
  public static long mod(long a, long b){
    if (a < b){
      return a;
    } else {
      return b + a % b;
    }
  }

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

  public static long phi(long n){
    long result = n;

    for (int i = 2, j = 4; j <= n; i++, j += i + i - 1){
      if (n % i == 0){
        result = result/i*(i - 1);
        while (n % i == 0){
          n /= i;
        }
      }
    }

    if (n > 1){
      result = result/n * (n - 1);
    }

    return result;
  }

  public static long [][] matrixPower(long I[][], long n, long m){
    long [][] T;

    if (n > 1){

      T = matrixPower(I, n/2, m);

      long a, b, c, d;
      a = T[0][0]; b = T[0][1];
      c = T[1][0]; d = T[1][1];
      T[0][0] = mod(a*a + b*c, m); T[0][1] = mod(a*b + b*d, m);
      T[1][0] = mod(c*a + d*c, m); T[1][1] = mod(c*b + d*d, m);

      if (n % 2 == 1){
        a = T[0][0]; b = T[0][1];
        c = T[1][0]; d = T[1][1];
        T[0][0] = mod(a*I[0][0] + b*I[1][0], m); T[0][1] = mod(a*I[0][1] + b*I[1][1], m);
        T[1][0] = mod(c*I[0][0] + d*I[1][0], m); T[1][1] = mod(c*I[0][1] + d*I[1][1], m);

      }

    } else {
      T = new long [2][2];
      T[0][0] = I[0][0]; T[0][1] = I[0][1];
      T[1][0] = I[1][0]; T[1][1] = I[1][1];
    }

    return T;
  }

  public static long f(long n, long a, long b, long p){
    if (n == 0){
      return a % p;
    } else if (n == 1){
      return b % p;
    } else if (a == 0 || b == 0){
      return 0;
    } else if (p == 1){
      return 0;
    }

    long [][] I = new long[2][2];
    long [][] A;
    I[0][0] = 1; I[0][1] = 1;
    I[1][0] = 1; I[1][1] = 0;

    long m = phi(p);
    A = matrixPower(I, n - 1, m);

    return (power(b, A[0][0], p)*power(a, A[0][1], p)) % p;
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    int T = r.nextPositiveInt();
    long a, b, p, n;

    for (int t = 1; t <= T; t++){
      a = r.nextPositiveLong();
      b = r.nextPositiveLong();
      p = r.nextPositiveLong();
      n = r.nextPositiveLong();

      sb.append("Case #");
      sb.append(t);
      sb.append(": ");
      sb.append(f(n - 1, a, b, p));
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
