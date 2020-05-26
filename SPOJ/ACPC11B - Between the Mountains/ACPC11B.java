/*
* Project name : SPOJ: ACPC11B - Between the Mountains
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-05-31
* Description  :
* Status       : Accepted (23854637)
* Tags         : java, fast I/O, floor binary search
* Comment      :
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;

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

final class ACPC11B{
  public static int minAltitudeDifference(int A[], int l, int r, int x){
    if (A[l] > x)
      return A[l] - x;

    int m, last = r - 1;
    while (r - l > 1){
      m = l + (r - l)/2;

      if (A[m] <= x)
        l = m;
      else
        r = m;
    }

    if (l < last){
      if (x - A[l] < A[l + 1] - x){
        return x - A[l];
      } else {
        return A[l + 1] - x;
      }
    } else {

      return x - A[l];
    }
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    int T = r.nextPositiveInt();
    int n, m, x, a, min_altitude_difference;
    int[] A = new int[1000];

    while (T-- > 0){
      n = r.nextPositiveInt();
      for (int i = 0; i < n; i++){
        A[i] = r.nextPositiveInt();
      }
      Arrays.sort(A, 0, n);

      m = r.nextPositiveInt();

      min_altitude_difference = 1000000;
      for (int i = 0; i < m; i++){
        a = r.nextPositiveInt();
        x = minAltitudeDifference(A, 0, n, a);

        if (x < min_altitude_difference){
          min_altitude_difference = x;
        }
      }

      sb.append(min_altitude_difference);
      sb.append('\n');
    }

    System.out.print(sb.toString());
  }
}
