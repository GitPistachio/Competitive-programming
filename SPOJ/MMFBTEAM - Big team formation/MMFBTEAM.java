/*
* Project name : SPOJ: MMFBTEAM - Big team formation
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-04-07
* Description  :
* Status       : Accepted (23592741)
* Tags         : java, fast I/O, integer sequence, combinatorics
* Comment      : 7.22 s
*/

import java.io.DataInputStream;
import java.io.IOException;
import java.math.BigInteger;

final class MMFBTEAM{
  static final class Reader{
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

    public byte readCharacter() throws IOException{
      byte c = read();
      while (c <= ' ')
          c = read();
      return c;
    }

    public String readLine() throws IOException{
      byte[] buf = new byte[64];
      int cnt = 0;
      byte c;
      while ((c = read()) != -1){
          if (c == '\n')
              break;
          buf[cnt++] = c;
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

    public int nextUnsignedInt() throws IOException{
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

  public static long power(long x, BigInteger n, long p){
    long result = 1;;
    BigInteger zero = BigInteger.valueOf(0);

    x = x % p;
    while (n.compareTo(zero) == 1){
      if (n.getLowestSetBit() == 0){
        result = (result * x) % p;
      }

      n = n.shiftRight(1);
      x = (x*x) % p;
    }

    return result;
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    BigInteger bin;
    long n;
    StringBuilder sb = new StringBuilder();
    long no_of_teams;
    long p = 1000000007;
    BigInteger bip = BigInteger.valueOf(p), two = BigInteger.valueOf(2);
    String token;

    while (!(token = r.readLine()).equals("0")){
      bin = new BigInteger(token);
      n = bin.mod(bip).longValue();
      no_of_teams = (((n*(n - 1)) % p) * power(2, bin.subtract(two), p)) % p;

      sb.append(no_of_teams);
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
