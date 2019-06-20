/*
* Project name : SPOJ: ACODE - Alphacode
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-20
* Description  :
* Status       : Accepted (23948820)
* Tags         : java, fast I/O, dynamic-programming
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

final class ACODE{
  public static final int MAX_SIZE = 5000;
  public static int n;
  public static byte[] line = new byte[MAX_SIZE];
  public static long[] results;

  public static long solve(int l) {
    if (results[l] != 0) {
      return results[l];
    }

    if (l == n) {
      results[l] = 1;
    } else if (l == n - 1) {
      if (line[l] >= '1') {
        results[l] = 1;
      } else {
        results[l] = -1;
      }
    } else if (line[l] == '0' || (line[l] >= '3' && line[l + 1] == '0')) {
      results[l] = -1;
    } else if (line[l] <= '2' && line[l + 1] == '0') {
      results[l] = solve(l + 2);
    } else if (line[l] == '1'|| (line[l] == '2' && line[l + 1] <= '6')) {
      long x = solve(l + 1), y = solve(l + 2);
      if (x > 0 && y > 0) {
        results[l] =  x + y;
      } else if (x > 0) {
        results[l] =  x;
      } else if (y > 0) {
        results[l] =  x;
      } else {
        results[l] = -1;
      }
    } else {
      results[l] = solve(l + 1);
    }
    return results[l];
  }

  public static long max(long x, long y) {
    if (x > y) {
      return x;
    }

    return y;
  }
  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();

    while (true) {
      n = r.readByteLine(line);
      results = new long[n + 1];
      if (line[0] == '0') {
        break;
      }

      sb.append(solve(0));
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
