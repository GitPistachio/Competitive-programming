/*
* Project name : SPOJ: FIBTWIST - Fibonacci With a Twist
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2019-06-11
* Description  : A(n) = F(n + 3) + F(n) - (n + 2) = 2*(F(n + 2) - 1) - n, where F is Fibonacci sequence
* Status       : Accepted (23907082)
* Tags         : java, fast I/O, fibonacci sequence, integer sequence A000045 (OEIS), partial sum of Fibonacci numbers, integer sequence A000071 (OEIS), integer sequence A001924 (OEIS), integer sequence A104161 (OEIS)
* Comment      :
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

final class FIBTWIST{
  public static long [][] matrixPower(long n, long p){
    long[][] T;

    if (n > 1){

      T = matrixPower(n/2, p);

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

  public static long fibonacci(long n, long p){
    if (n > 0){
      return matrixPower(n - 1, p)[0][0];
    }

    return 0;
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    int n, p, T = r.nextPositiveInt();
    long result;

    while (T-- > 0){
      n = r.nextPositiveInt();
      p = r.nextPositiveInt();

      result = (2*(fibonacci(n + 2, p) - 1) - n) % p;
      if (result < 0){
      	result += p;
      }
      sb.append(result);
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
