/*
* Project name : SPOJ: SPCQ - Gopu and Digits Divisibility
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2019-06-17
* Description  :
* Status       : Accepted (23929560)
* Tags         : java, fast I/O, Niven (Harshad) numbers A005349 (OEIS), brute force
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

  public String nextWord() throws IOException {
    byte[] buf = new byte[10];
    int cnt = 0;
    byte c = read();

    while (c <= ' ')
      c = read();

    buf[cnt++] = c;
    while ((c = read()) != -1) {
      if (c <= ' ') {
        break;
      }

      buf[cnt++] = c;
    }
    return new String(buf, 0, cnt);
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

final class SPCQ{
  public static long sumOfDigits(long n){
    long sum_of_digits = 0;

    while (n > 0){
      sum_of_digits += n % 10;
      n /= 10;
    }

    return sum_of_digits;
  }
  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    int T = r.nextPositiveInt();
    long n, sum_of_digits;

    while (T-- > 0){
      n = r.nextPositiveLong();

      while (n % sumOfDigits(n++) != 0);

      sb.append(n - 1);
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
