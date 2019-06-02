/*
* Project name : SPOJ: YODANESS - Yodaness Level
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-01
* Description  :
* Status       : Accepted (23863331)
* Tags         : java, fast I/O, merge sort, inverse count, sorting, map
* Comment      : The main algorith is the same as in INVCNT
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;
import java.util.Map;
import java.util.HashMap;

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

  public String nextWord() throws IOException{
    byte[] buf = new byte[30];
    int cnt = 0;
    byte c;
    while ((c = read()) != -1){
      if (c <= ' '){
        if (cnt > 0){
          break;
        }
      } else {
        buf[cnt++] = c;
      }
    }

    return new String(buf, 0, cnt);
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

final class YODANESS{
  public static long merge(int A[], int p, int q, int r){
    int i = p, k = 0, j = q;
    long inv_count = 0;
    int[] T = new int[r - p + 1];

    while (i <= q - 1 && j <= r){
      if (A[i] <= A[j]){
          T[k] = A[i];
          i += 1;
      }
      else{
          T[k] = A[j];
          j += 1;
          inv_count += q - i;
      }
      k += 1;
    }

    if (i <= q - 1){
      while (i <= q - 1){
        T[k] = A[i];
        i += 1;
        k += 1;
      }
    }
    else{
      while (j <= r){
        T[k] = A[j];
        j += 1;
        k += 1;
      }
    }

    for (i = 0; i < r - p + 1; i++){
      A[p + i] = T[i];
    }

    return inv_count;
  }

  public static long mergeSort(int A[], int p, int r){
    long inv_count = 0;
    int q;

    if (p < r){
      q = (p + r)/2;
      inv_count += mergeSort(A, p, q);
      inv_count += mergeSort(A, q + 1, r);
      inv_count += merge(A, p, q + 1, r);
    }
    return inv_count;
  }
  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    int n, T = r.nextPositiveInt();
    Map<String, Integer> words = new HashMap<>();
    int[] A;

    while (T-- > 0){
      n = r.nextPositiveInt();
      A = new int[n];
      for (int i = 0; i < n; i++){
          words.put(r.nextWord(), i);
      }
      for (int i = 0; i < n; i++){
          A[i] = words.get(r.nextWord());
      }

      sb.append(mergeSort(A, 0, n - 1));
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
