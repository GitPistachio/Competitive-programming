/*
* Project name : SPOJ: MATHII - Yet Another Mathematical Problem
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-19
* Description  :
* Status       : Accepted (23945545)
* Tags         : java, fst I/O, math, integer sequence A061201 (OEIS), integer sequence A006218 (OEIS)
* Comment      :
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;
import java.lang.Math;

final class Reader{
  final private int BUFFER_SIZE = 1 << 16;
  private DataInputStream dis;
  private byte[] buffer;
  private int bufferPointer, bytesRead;
  public boolean EOF = false;

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
    if (EOF) return -1;

    long ret = 0;
    byte c = read();
    while (c <= ' ' && !EOF)
      c = read();
      //System.out.println(c + " " + EOF);
    do{
        ret = ret * 10 + c - '0';
    }  while ((c = read()) >= '0' && c <= '9' && !EOF);

    return ret;
  }

  public int nextPositiveInt() throws IOException{
    if (EOF) return -1;

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
          EOF = true;
      }
  }

  private byte read() throws IOException{
    if (EOF) return -1;

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
  public static long b(long n) {
    long n2 = (long) Math.floor(Math.sqrt(n));
    long x = 0;

    for (int i = 1; i <= n2; i++) {
      x += n/i;
    }

    //System.out.println(n + " " + ((x << 1) - n2*n2));
    return (x << 1) - n2*n2;
  }

  public static long a(long n) {
    long n3 = (long) Math.floor(Math.cbrt(n));
    long n2, c = 0, x = 0;

    for (int i = 1; i <= n3; i++) {
      c += b(n/i);
    }

    for (int i = 1; i <= n3; i++) {
      for (int j = i + 1; j <= n3; j++) {
        x += n/(i*j);
      }
      c -= n/(i*i);
    }

    c -= x << 1;

    return 3*c + n3*n3*n3;
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    long n;
    int t = 0;

    while ((n = r.nextPositiveLong()) > 0) {
      //System.out.println(n);
      sb.append("Case ");
      sb.append(++t);
      sb.append(": ");
      sb.append(a(n));
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
