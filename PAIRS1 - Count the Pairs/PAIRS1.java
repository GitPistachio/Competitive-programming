/*
* Project name : SPOJ: PAIRS1 - Count the Pairs
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-20
* Description  :
* Status       : Accepted (23947905)
* Tags         : java, fast I/O, sorting, binary search
* Comment      :
*/

import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;

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

final class MATHII{
  public static boolean binary_search(int A[], int l, int r, int x) {
    int m;
    while (l <= r) {
      m = l + ((r - l) >> 1);
      if (A[m] == x) {
        return true;
      }
      if (A[m] < x) {
        l = m + 1;
      } else {
        r = m - 1;
      }
    }

    return false;
  }
  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    final int MAX_SIZE = 100000;
    int n = r.nextPositiveInt(), d = r.nextInt();
    int[] A = new int[MAX_SIZE];
    int cnt = 0;

    for (int i = 0; i < n; i++) {
      A[i] = r.nextInt();
    }

    Arrays.sort(A, 0, n);

    for (int i = 0; i < n - 1; i++) {
      if (binary_search(A, i + 1, n - 1, A[i] + d)) {
        cnt++;
      }
    }
    System.out.println(cnt);
  }
}
