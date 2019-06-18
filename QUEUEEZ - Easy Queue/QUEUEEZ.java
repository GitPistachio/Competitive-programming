/*
* Project name : SPOJ: QUEUEEZ - Easy Queue
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-17
* Description  :
* Status       : Accepted (23933288)
* Tags         : java, fast I/O, queue
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

  private void fillBuffer() throws IOException {
      bytesRead = dis.read(buffer, bufferPointer = 0, BUFFER_SIZE);
      if (bytesRead == -1)
          buffer[0] = -1;
  }

  public byte nextByte() throws IOException {
    byte c;
    while ((c = read()) <= ' ');

    return c;
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

final class QUEUEEZ{
  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    final int MAX_SIZE = 1000000;
    int T = r.nextPositiveInt();
    int front = 0, back = 0;
    byte type_of_operation;
    int[] st = new int[MAX_SIZE];

    while (T-- > 0){
      type_of_operation = r.nextByte();

      if (type_of_operation == '1') {
        st[back++] = r.nextInt();
      } else if (type_of_operation == '2') {
        if (back > front) {
          front++;
        } else {
          back = 0;
          front = 0;
        }
      } else {
        if (back > front) {
          sb.append(st[front]);
          sb.append('\n');
        } else {
          sb.append("Empty!\n");
        }
      }
    }
    System.out.print(sb.toString());
  }
}
