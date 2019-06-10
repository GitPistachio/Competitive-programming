/*
* Project name : SPOJ: SUMFOUR - 4 values whose sum is 0
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-10
* Description  :
* Status       : Accepted (23903531)
* Tags         : java, Fast I/O, linear Diophantine equation, floor binary search, binary search
* Comment      :
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;

final class Reader{
  final private int BUFFER_SIZE = 1 << 16;
  private DataInputStream dis;
  private byte[] buffer, token;
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

final class SUMFOUR{
  public static int floorBinarySearch(int A[], int l, int r, int key){
    if (A[l] > key)
      return -1;

    int m;
    while (r - l > 1){
      m = l + (r - l)/2;

      if (A[m] <= key)
        l = m;
      else
        r = m;
    }
    return l;
  }

  public static int noOfOccurences(int a, int A[], int l, int r){
    int m, no_of_occurences = 0, mm, ml = l, mr = r;

    while (l <= r){
      m = l + (r - l)/2;

      if (A[m] == a){
        no_of_occurences = 1;
        mm = m;

        while (m-- > ml && A[m] == a){
          no_of_occurences++;
        }

        m = mm;
        while (m++ < mr && A[m] == a){
          no_of_occurences++;
        }

        break;
      } else if (A[m] > a){
        r = m - 1;
      } else {
        l = m + 1;
      }
    }

    return no_of_occurences;
  }
  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    int m, no_of_quadruplet = 0, n = r.nextPositiveInt(), n2 = n*n, zero_idx;
    Integer no_of_duplets;
    int[] A = new int[n];
    int[] B = new int[n];
    int[] C = new int[n];
    int[] D = new int[n];
    int[] LHS = new int[n2];
    int[] RHS = new int[n2];

    for (int i = 0; i < n; i++){
      A[i] = r.nextInt();
      B[i] = r.nextInt();
      C[i] = r.nextInt();
      D[i] = r.nextInt();
    }

    m = 0;
    for (int i = 0; i < n; i++){
      for (int j = 0; j < n; j++){
        LHS[m] = A[i] + B[j];
        RHS[m++] = -(C[i] + D[j]);
      }
    }

    Arrays.sort(RHS);
    zero_idx = floorBinarySearch(RHS, 0, n2 - 1, -1);

    for (int i = 0; i < n2; i++){
      if (LHS[i] < 0){
        if (zero_idx > -1){
          no_of_quadruplet += noOfOccurences(LHS[i], RHS, 0, zero_idx);
        }
      } else {
        no_of_quadruplet += noOfOccurences(LHS[i], RHS, zero_idx + 1, n2 - 1);
      }
    }

    System.out.println(no_of_quadruplet);
  }
}
