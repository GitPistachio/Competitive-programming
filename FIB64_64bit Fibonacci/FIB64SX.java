/*
* Project name : SPOJ: FIB64 - 64bit Fibonacci
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-18
* Description  :
* Status       : Accepted (23939458)
* Tags         : java, math, fast I/O fibonacci sequence
* Comment      : 12000
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;
import java.lang.Math;
import java.math.BigInteger;

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

class FIB64S6{
  public static boolean[] bits = new boolean[63];

  public static BigInteger moduloFibonacci(long n, BigInteger m){
    BigInteger v1 = BigInteger.valueOf(1);
    BigInteger v2 = BigInteger.valueOf(1);
    BigInteger v3 = BigInteger.valueOf(0);
    BigInteger t, tv1;
    int no_of_bits = 0;

    while (n > 0){
      bits[no_of_bits++] = ((n & 1) == 1);
      n >>= 1;
    }

    for (int i = no_of_bits - 2; i >= 0; i--) {
      t = v2.multiply(v2).mod(m);
      tv1 = v1.multiply(v1).add(t).mod(m);
      v2 = v1.add(v3).multiply(v2).mod(m);
      v3 = v3.multiply(v3).add(t).mod(m);
      v1 = tv1;

      if (bits[i]){
        v3 = v2;
        v2 = v1;
        v1 = v2.add(v3).mod(m);
      }
    }

    return v2;
}

  public static void main(String args[]) throws IOException {
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    long n;
    BigInteger m;

    for (int i = 0; i < 12000; i++){
      n = r.nextPositiveLong();
      m = BigInteger.valueOf(r.nextPositiveLong());

      if (n > 1){
        sb.append(moduloFibonacci(n, m));
      } else {
        sb.append(n);
      }
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
