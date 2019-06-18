/*
* Project name : SPOJ: MATEX - Matrix Exponentiation
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-18
* Description  :
* Status       : Accepted (23938295)
* Tags         : java, fast I/O, matrix, matrix exponentiation
* Comment      : 620
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

final class MATEX{
  private static long[][][] L;
  public static long[][] naiveSquareMatrixMultiplication(long A[][], long B[][], int n, long p) {
    long[][] C = new long[n][n];

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        for (int k = 0; k < n; k++) {
          C[i][j] += (A[i][k]*B[k][j] % p);
        }
        C[i][j] = C[i][j] % p;
      }
    }

    return C;
  }

  public static long[][] naiveMatrixExpotentation(long A[][], int n, long m, long p) {
    if (m > 1) {
      long[][] M = naiveMatrixExpotentation(A, n, m/2, p);
      if ((m & 1) == 0) {
        return naiveSquareMatrixMultiplication(M, M, n, p);
      } else {
        return naiveSquareMatrixMultiplication(naiveSquareMatrixMultiplication(M, M, n, p), A, n, p);
      }
    }

    return A;
  }

  public static long[][] iterativeMatrixExpotentation(int n, long m, long p) {
    long[][] M;
    int i = 0;

    while ((m & 1) != 1) {
      i++;
      m >>= 1;
    }
    M = L[i];

    while (m > 0) {
      m >>= 1;
      i++;
      if ((m & 1) == 1) {
        M = naiveSquareMatrixMultiplication(M, L[i], n, p);
      }
    }

    return M;
  }

  public static long iterativeMatrixExpotentationOptimized(int row, int col, int n, long m, long p) {
    long[][] M;
    int i = 0;
    long a = 0;

    while ((m & 1) != 1) {
      i++;
      m >>= 1;
    }
    M = L[i];

    while (m > 3) {
      m >>= 1;
      i++;
      if ((m & 1) == 1) {
        M = naiveSquareMatrixMultiplication(M, L[i], n, p);
      }
    }

    m >>= 1;
    if ((m & 1) == 1) {
      i++;
      for (int j = 0; j < n; j++) {
        a += (M[row][j]*L[i][j][col]) % p;
      }

      return a % p;
    } else {
      return M[row][col];
    }
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    final long p = 1000000007;
    final int max_no_of_queries = 620;
    int row, col, n = r.nextPositiveInt();
    long[][] M = new long[n][n];
    L = new long[63][n][n];
    long m;

    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++) {
        M[i][j] = r.nextPositiveInt();
      }
    }

    L[0] = M;
    for (int i = 1; i < 63; i++) {
        L[i] = naiveSquareMatrixMultiplication(L[i - 1], L[i - 1], n, p);
    }


    for (int i = 0; i < max_no_of_queries; i++) {
      row = r.nextPositiveInt() - 1;
      col = r.nextPositiveInt() - 1;
      m = r.nextPositiveLong();

      sb.append(iterativeMatrixExpotentationOptimized(row, col, n, m, p));
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
