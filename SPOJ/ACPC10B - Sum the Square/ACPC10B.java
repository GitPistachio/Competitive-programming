/*
* Project name : SPOJ: ACPC10B - Sum the Square
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-05-18
* Description  :
* Status       : Accepted (23783124)
* Tags         : java, fast I/O, number theory, sum of squares of digits of previous term
* Comment      :
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

final class ACPC10B{
  public static int sumOfDigitSquares(int n){
    int result = 0;
    int r;

    while (n > 0){
      r = n % 10;
      result += r*r;
      n /= 10;
    }

    return result;
  }

  public static boolean isInLoop(int n){
    if (n == 1 || n == 4 || n == 16 || n == 20 || n == 37 || n == 42 || n == 58 || n == 89 || n == 145){
      return true;
    }

    return false;
  }
  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();

    int a, b;
    int n = 0, m = 0, l;
    int [] A = new int[50];
    int [] B = new int[50];
    int [] loop = new int [146];
    loop[4] = 16; loop[16] = 37; loop[37] = 58; loop[58] = 89; loop[89] = 145; loop[145] = 42; loop[42] = 20; loop[20] = 4;
    boolean matched, b_in_loop, a_in_loop;

    while (true){
      a = r.nextPositiveInt();
      b = r.nextPositiveInt();
      if (a == 0 && b == 0) break;

      l = 30;
      m = 0;
      n = 0;
      matched = false;
      a_in_loop = false;
      b_in_loop = false;

      A[0] = a;
      a_in_loop = isInLoop(a);
      if (a_in_loop && A[n] != 1){
        for (int i = 0; i < 7; i++){
          A[n + 1] = loop[A[n]];
          n++;
        }
      }
      B[0] = b;
      b_in_loop = isInLoop(b);
      if (b_in_loop && B[m] != 1){
        for (int i = 0; i < 7; i++){
          B[m + 1] = loop[B[m]];
          m++;
        }
      }
      n++;
      m++;
      for (int t = 1; (!a_in_loop || !b_in_loop); t++){
        if (!a_in_loop){
          A[n] = sumOfDigitSquares(A[n - 1]);
          a_in_loop = isInLoop(A[n]);
          if (a_in_loop && A[n] != 1){
            for (int i = 0; i < 7; i++){
              A[n + 1] = loop[A[n]];
              n++;
            }
          }
          n++;
        }
        if (!b_in_loop){
          B[m] = sumOfDigitSquares(B[m - 1]);
          b_in_loop = isInLoop(B[m]);
          if (b_in_loop && B[m] != 1){
            for (int i = 0; i < 7; i++){
              B[m + 1] = loop[B[m]];
              m++;
            }
          }
          m++;
        }
      }

      for (int i = 0; i < n; i++){
        for (int j = 0; j < m; j++){
          if (l <= i + j + 2) break;
          if (A[i] == B[j]){
            matched = true;
            l = i + j + 2;
            break;
          }
        }
      }

      if (!matched){
        l = 0;
      }

      sb.append(a);
      sb.append(' ');
      sb.append(b);
      sb.append(' ');
      sb.append(l);
      sb.append('\n');
    }

    System.out.print(sb.toString());
  }
}
