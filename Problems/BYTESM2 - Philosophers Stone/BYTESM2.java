/*
* Project name : SPOJ: BYTESM2 - Philosophers Stone
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-21
* Description  :
* Status       : Accepted (23955080)
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

final class SPOJ{
  public static final int MAX_SIZE = 100;
  public static int n, m;
  public static int[][] grid = new int[MAX_SIZE][MAX_SIZE];
  public static int[][] result = new int[MAX_SIZE][MAX_SIZE];

  public static int solve() {
    int max_no_of_stones;

    for (int j = 0; j < m; j++) {
      result[n - 1][j] = grid[n - 1][j];
    }


    for (int i = n - 2; i >= 0; i--) {
      result[i][0] = grid[i][0] + max(result[i + 1][0], result[i + 1][1]);
      result[i][m - 1] = grid[i][m - 1] + max(result[i + 1][m - 2], result[i + 1][m - 1]);
      for (int j = 1; j < m - 1; j++) {
        result[i][j] = grid[i][j] + max(result[i + 1][j - 1], max(result[i + 1][j], result[i + 1][j + 1]));
      }
    }

    max_no_of_stones = result[0][0];

    for (int j = 1; j < m; j++) {
      if (max_no_of_stones < result[0][j]) {
        max_no_of_stones = result[0][j];
      }
    }


    return max_no_of_stones;
  }

  public static int max(int x, int y) {
    if (x > y) {
      return x;
    }
    return y;
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    int T = r.nextNonNegativeInt();

    while (T-- > 0) {
      n = r.nextNonNegativeInt();
      m = r.nextNonNegativeInt();

      for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
          grid[i][j] = r.nextNonNegativeInt();
        }
      }

      sb.append(solve());
      sb.append('\n');
    }

    System.out.print(sb.toString());
  }
}
