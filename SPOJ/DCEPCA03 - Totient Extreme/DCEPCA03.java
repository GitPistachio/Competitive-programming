/*
* Project name : SPOJ: DCEPCA03 - Totient Extreme
* Author       : Wojciech Raszka
* E-amil       : gitpistachio@gmail.com
* Date created : 2019-05-15
* Description  :
* Status       : Accepted (23770540)
* Tags         : java, Euler's totient function, integer sequence A002088 (OEIS), short multiplication formulas
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

final class DCEPCA03{
  final static int [] primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};

  public static int phi(int n){
    int result = n;

    for (int p : primes){
      if (p*p > n) break;
      if (n % p == 0){
        result -= result/p;

        n /= p;
        while (n % p == 0){
          n /= p;
        }
      }
    }

    if (n > 1){
      result -= result/n;
    }

    return result;
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    int T = r.nextPositiveInt(), n;
    int MAX_N = 1;
    int [] A = new int[T];


    for (int t = 0; t < T; t++){
      A[t] = r.nextPositiveInt();

      if (A[t] > MAX_N){
        MAX_N = A[t];
      }
    }

    int [] HR = new int [MAX_N + 1];

    for (int i = 1; i <= MAX_N; i++){
      HR[i] = HR[i - 1] + phi(i);
    }

    for (int t = 0; t < T; t++){
      sb.append(HR[A[t]]*(long)HR[A[t]]);
      sb.append('\n');
    }

    System.out.print(sb.toString());
  }
}
