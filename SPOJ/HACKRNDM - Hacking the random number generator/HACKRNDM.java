/*
* Project name : SPOJ: HACKRNDM - Hacking the random number generator
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-20
* Description  :
* Status       : Accepted (23947165)
* Tags         : java, fast I/O, sorting, sliding window algorithm
* Comment      :
*/

import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;

final class Reader{
  final private int BUFFER_SIZE = 1 << 14;
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

final class HACKRNDM{
  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    int n = r.nextNonNegativeInt(), d = r.nextNonNegativeInt();
    int[] A = new int[n];
    int j = 1, cnt = 0, ccnt = 0;

    for (int i = 0; i < n; i++) {
      A[i] = r.nextNonNegativeInt();
    }

    Arrays.sort(A);

    for (int i = 0; i < n - 1; i++) {
      ccnt = 0;
      while (j < n && A[j] - A[i] < d) {
        j++;
      }

      while (j < n && A[j] - A[i] == d) {
        ccnt++;
        j++;
      }

      cnt += ccnt;

      if (j >= n) {
        break;
      }
    }

    System.out.println(cnt);
  }
}
