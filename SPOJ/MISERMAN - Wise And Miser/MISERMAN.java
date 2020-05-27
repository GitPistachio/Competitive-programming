/*
* Project name : SPOJ: MISERMAN - Wise And Miser
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-21
* Description  :
* Status       : Accepted (23954821)
* Tags         : java, fast I/O, dynamic programming
* Comment      :
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;

final class Reader{
  final private int BUFFER_SIZE = 1 << 13;
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

  public int readByteLine(byte line[]) throws IOException {
      int cnt = 0;
      byte c;
      while ((c = read()) != -1) {
          if (c == '\n')
              break;
          line[cnt++] = c;
      }
      return cnt;
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

  public long nextNonNegativeLong() throws IOException{
    long ret = 0;
    byte c = read();
    while (c <= ' ')
      c = read();
    do{
        ret = ret * 10 + c - '0';
    }  while ((c = read()) >= '0' && c <= '9');

    return ret;
  }

  public int nextNonNegativeInt() throws IOException{
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
      if (bytesRead == -1) {
          buffer[0] = -1;
      }
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

final class ACPC10D{
  public static final int MAX_SIZE = 100;
  public static int n, m;
  public static long[][] grid = new long[MAX_SIZE][MAX_SIZE];
  public static long[][] result = new long[MAX_SIZE][MAX_SIZE];

  public static long solve() {
    long min_cost;

    for (int j = 0; j < n; j++) {
      result[n - 1][j] = grid[n - 1][j];
    }


    for (int i = n - 2; i >= 0; i--) {
      result[i][0] = grid[i][0] + min(result[i + 1][0], result[i + 1][1]);
      result[i][n - 1] = grid[i][n - 1] + min(result[i + 1][n - 2], result[i + 1][n - 1]);
      for (int j = 1; j < n - 1; j++) {
        result[i][j] = grid[i][j] + min(result[i + 1][j - 1], min(result[i + 1][j], result[i + 1][j + 1]));
      }
    }

    min_cost = result[0][0];

    for (int j = 1; j < n; j++) {
      if (min_cost > result[0][j]) {
        min_cost = result[0][j];
      }
    }


    return min_cost;
  }

  public static long min(long x, long y) {
    if (x < y) {
      return x;
    }
    return y;
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();

    n = r.nextNonNegativeInt();
    m = r.nextNonNegativeInt();

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < m; j++) {
        grid[i][j] = r.nextNonNegativeLong();
      }
    }

    sb.append(solve());
    sb.append('\n');
    System.out.print(sb.toString());
  }
}
