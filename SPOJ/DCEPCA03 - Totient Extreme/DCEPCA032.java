/*
* Project name : SPOJ: DCEPCA03 - Totient Extreme
* Author       : Wojciech Raszka
* E-amil       : gitpistachio@gmail.com
* Date created : 2019-05-15
* Description  :
* Status       : Accepted (23770603)
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
    int [] PHI = new int [MAX_N + 1];

    PHI[1] = 1;
    HR[1] = PHI[1];

    for (int i = 2; i <= MAX_N; i++){
      if (PHI[i] == 0){
        PHI[i] = i - 1;
        for (int j = (i << 1); j <= MAX_N; j += i){
          if (PHI[j] == 0){
            PHI[j] = j;
          }
          PHI[j] = (PHI[j]/i)*(i - 1);
        }
      }
      HR[i] = HR[i - 1] + PHI[i];
    }

    for (int t = 0; t < T; t++){
      sb.append(HR[A[t]]*(long)HR[A[t]]);
      sb.append('\n');
    }

    System.out.print(sb.toString());
  }
}
