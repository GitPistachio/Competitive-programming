/*
* Project name : SPOJ: FIBOSUM - Fibonacci Sum
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-11
* Description  : A(n) = b*F(n + 2) + a*F(n + 1) - b , where F is Fibonacci sequence
* Status       : Accepted (23906688)
* Tags         : java, fast I/O, fibonacci sequence A000045 (OEIS), partial sum of Fibonacci numbers A000071 (OEIS)
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

final class FIBOSUM{
  public static long [][] matrixPower(long I[][], long n, long p){
    long[][] T;

    if (n > 1){

      T = matrixPower(I, n/2, p);

      long a, b, c, d;
      a = T[0][0]; b = T[0][1];
      c = T[1][0]; d = T[1][1];
      T[0][0] = (a*a + b*c) % p; T[0][1] = (a*b + b*d) % p;
      T[1][0] = (c*a + d*c) % p; T[1][1] = (c*b + d*d) % p;

      if (n % 2 == 1){
        a = T[0][0]; b = T[0][1];
        c = T[1][0]; d = T[1][1];
        T[0][0] = (a*I[0][0] + b*I[1][0]) % p; T[0][1] = (a*I[0][1] + b*I[1][1]) % p;
        T[1][0] = (c*I[0][0] + d*I[1][0]) % p; T[1][1] = (c*I[0][1] + d*I[1][1]) % p;

      }

    } else {
      T = new long [2][2];
      T[0][0] = I[0][0]; T[0][1] = I[0][1];
      T[1][0] = I[1][0]; T[1][1] = I[1][1];
    }

    return T;
  }

  public static long fibonacci(long n, long first, long second, long p){
    if (n > 2){
      long[][] T, I = new long [2][2];
      I[0][0] = 1; I[0][1] = 1;
      I[1][0] = 1; I[1][1] = 0;

      T = matrixPower(I, n - 1, p);


      return (second*T[0][0] + first*T[1][0]) % p;
    } else if (n == 2){
      return (second + first) % p;
    } else if (n == 1){
      return second % p;
    }

    return first;
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    int first, second, n, T = r.nextPositiveInt();
    long p, result;

    while (T-- > 0){
      first = r.nextPositiveInt();
      second = r.nextPositiveInt();
      n = r.nextPositiveInt();
      p = r.nextPositiveInt();

      result = (fibonacci(n + 1, first, second, p) - (second % p)) % p;
      if (result < 0){
      	result += p;
      }

      sb.append(result);
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
