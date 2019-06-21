/*
* Project name : SPOJ: ACPC10D - Tri graphs
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-21
* Description  :
* Status       : Accepted (23954767)
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
  public static final int MAX_SIZE = 100000;
  public static int n;
  public static long[][] grid = new long[MAX_SIZE][3];
  public static long[][] result = new long[MAX_SIZE][3];

  public static long solve(int i, int j) {
    if (i == n - 2) {
      if (j == 2) {
        return grid[i][j] + grid[i + 1][1];
      } else if (j == 1) {
        return grid[i][j] + grid[i + 1][1] + min(0, min(grid[i][2], grid[i + 1][0]));
      } else {
        return grid[i][j] + grid[i + 1][1] + min(0, min(grid[i + 1][0], min(grid[i][1], grid[i][1] + grid[i][2])));
      }
    } else {
      if (j == 0){
        return grid[i][j] + min(solve(i, 1), min(solve(i + 1, 0), solve(i + 1, 1)));
      } else if (j == 1){
        return grid[i][j] + min(solve(i, 2), min(solve(i + 1, 0), min(solve(i + 1, 1), solve(i + 1, 2))));
      } else {
        return grid[i][j] + min(solve(i + 1, 1), solve(i + 1, 2));
      }
    }
  }

  public static long solvedp(int r, int c) {
    result[n - 1][0] = grid[n - 1][0] + grid[n - 1][1]; result[n - 1][1] = grid[n - 1][1];
    result[n - 2][2] = grid[n - 2][2] + grid[n - 1][1];
    result[n - 2][1] = grid[n - 2][1] + grid[n - 1][1] + min(0, min(grid[n - 2][2], grid[n - 1][0]));
    result[n - 2][0] = grid[n - 2][0] + grid[n - 1][1] + min(0, min(grid[n - 1][0], min(grid[n - 2][1], grid[n - 2][1] + grid[n - 2][2])));

    for (int i = n - 3; i >= 0; i--) {
      result[i][2] = grid[i][2] + min(result[i + 1][1], result[i + 1][2]);
      result[i][1] = grid[i][1] + min(result[i][2], min(result[i + 1][0], min(result[i + 1][1], result[i + 1][2])));
      result[i][0] = grid[i][0] + min(result[i][1], min(result[i + 1][0], result[i + 1][1]));
    }

    return result[r][c];
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
    int t = 1;

    while ((n = r.nextNonNegativeInt()) > 0) {
      for (int i = 0; i < n; i++) {
        grid[i][0] = r.nextInt(); grid[i][1] = r.nextInt(); grid[i][2] = r.nextInt();
      }

      sb.append(t++);
      sb.append(". ");
      sb.append(solvedp(0, 1));
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
