/*
* Project name : SPOJ: ACPC11C - Circleland
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-05-31
* Description  :
* Status       : Accepted (23856523)
* Tags         : java, fast I/O, prefix sum
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

final class ACPC11C{
  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    int T = r.nextPositiveInt();
    int n, x, min_total_dist;
    int[] A = new int[100001];

    while (T-- > 0){

      n = r.nextPositiveInt();
      for (int i = 1; i <= n; i++){
        A[i] = A[i - 1] + r.nextPositiveInt();
      }

      min_total_dist = A[n - 1];
      if (A[n] - A[1] < min_total_dist){
        min_total_dist = A[n] - A[1];
      }

      for (int i = 1; i < n - 1; i++){
        x = 2*A[i] + A[n] - A[i + 1];
        if (x < min_total_dist){
          min_total_dist = x;
        }

        x = 2*(A[n] - A[n - i]) + A[n - i - 1];
        if (x < min_total_dist){
          min_total_dist = x;
        }
      }

      sb.append(min_total_dist);
      sb.append('\n');
    }

    System.out.print(sb.toString());
  }
}
