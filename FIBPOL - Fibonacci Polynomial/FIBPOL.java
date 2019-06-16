/*
* Project name : SPOJ: FIBPOL - Fibonacci Polynomial
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-13
* Description  :
* Status       : Accepted (23915114)
* Tags         : java, fast I/O, fibonacci sequence A000045 (OEIS), integer sequence A081018 (OEIS)
* Comment      :
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;
import java.util.Set;
import java.util.HashSet;

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

final class FIBTWIST{
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

  public static long [][] fibonacciMatrixPower(long n){
    long[][] T;

    if (n > 1){

      T = fibonacciMatrixPower(n/2);

      long a, b, c, d;
      a = T[0][0]; b = T[0][1];
      c = T[1][0]; d = T[1][1];
      T[0][0] = (a*a + b*c); T[0][1] = (a*b + b*d);
      T[1][0] = (c*a + d*c); T[1][1] = (c*b + d*d);

      if (n % 2 == 1){
        a = T[0][0]; b = T[0][1];
        c = T[1][0]; d = T[1][1];
        T[0][0] = (a + b); T[0][1] = a;
        T[1][0] = (c + d); T[1][1] = c;

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
    final long MAX_AX = 100000000000000000L;
    long n, Ax, x, a = 0, b = 1;
    long[][] F;
    Set<Long> A = new HashSet<Long>();

    while (true){
      x = a*b;

      A.add(x);
      if (x > MAX_AX) break;

      a = a + b;
      b = a + b;
    }

    while (T-- > 0){
      Ax = r.nextPositiveLong();
      if (A.contains(Ax)){
        sb.append("1\n");
      } else {
        sb.append("0\n");
      }
    }
    System.out.print(sb.toString());
  }
}
