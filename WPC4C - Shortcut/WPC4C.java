/*
* Project name : SPOJ: WPC4C - Shortcut
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-04
* Description  :
* Status       : Accepted (23879285)
* Tags         : java, fast I/O, rectangle
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


final class VFMUL{
  public static long min(long x, long y){
    if (x < y){
      return x;
    } else {
      return y;
    }
  }
  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    int T = r.nextPositiveInt();
    long height, width, x, y, max_area, max_height, max_width;

    while (T-- > 0){
      x = r.nextPositiveLong();
      y = r.nextPositiveLong();

      height = 1;
      max_area = 0;
      max_height = 1;
      max_width = 1;
      while (height <= x){
        width = min(5*height/4, y);
        if (5*width >= 4*height){
          if (max_area <= width*height){
            max_area = width*height;
            max_width = width;
            max_height = height;
          }
        }
        height <<= 1;
      }

      width = 1;
      while (width <= y){
        height = min(5*width/4, x);
        if (5*width >= 4*height){
          if (max_area < width*height){
            max_area = width*height;
            max_width = width;
            max_height = height;
          } else if (max_area == width*height && height > max_height){
            max_width = width;
            max_height = height;
          }
        }
        width <<= 1;
      }

      sb.append(max_height);
      sb.append(' ');
      sb.append(max_width);
      sb.append('\n');
    }

    System.out.print(sb.toString());
  }
}
