/*
* Project name : SPOJ: MMFTEAM - Team formation
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-04-09
* Description  :
* Status       : Accepted (23607271)
* Tags         : java, fast I/O, integer sequence, combinatorics
* Comment      :
*/

import java.io.DataInputStream;
import java.io.IOException;

final class MMFTEAM{
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

  public static long power(long x, long y, long p){
    long result = 1;

    x = x % p;
    while (y > 0){
      if ((y & 1) == 1){
        result = (result * x) % p;
      }

      y = y >> 1;
      x = (x*x) % p;
    }

    return result;
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    long no_of_teams;
    long n, p = 1000000007;

    while ((n = r.nextUnsignedInt()) != 0){
      no_of_teams = (((n*(n - 1)) % p) * power(2, n - 2, p)) % p;

      sb.append(no_of_teams);
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
