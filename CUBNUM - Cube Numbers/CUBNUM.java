/*
* Project name : SPOJ: CUBNUM - Cube Numbers
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-04-06
* Description  :
* Status       : Accepted (23582699)
* Tags         : java, fast I/O, math, dynamic programming, number theory, integer sequence A002376 (OEIS)
* Comment      :
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;

final class CUBNUM{
  static final class Reader{
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

      public int nextUnsignedInt() throws IOException{
          if (EOF) return -1;

          int ret = 0;
          byte c = read();

          do{
              ret = ret * 10 + c - '0';
          }  while ((c = read()) >= '0' && c <= '9');

          return ret;
      }

      private void fillBuffer() throws IOException{
          bytesRead = dis.read(buffer, bufferPointer = 0, BUFFER_SIZE);
          if (bytesRead == -1){
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

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    int n;
    final int MAX_N = 100000;
    byte[] no_of_cubes = new byte[MAX_N + 1];
    byte min_no_of_cubes;
    int cube;
    int t;

    for (n = 1; n <= MAX_N; n++){
      min_no_of_cubes = 127;
      for (int i = 1; i < 48; i++){
        cube = i*i*i;
        if (cube < n){
          if (min_no_of_cubes > no_of_cubes[n - cube]){
            min_no_of_cubes = no_of_cubes[n - cube];
          }
        } else if (cube == n){
          no_of_cubes[n] = 1;
          break;
        } else {
          no_of_cubes[n] = (byte) (1 + min_no_of_cubes);
          break;
        }
      }
    }

    t = 1;
    while ((n = r.nextUnsignedInt()) > 0){
      sb.append("Case #");
      sb.append(t);
      sb.append(": ");
      sb.append(no_of_cubes[n]);
      sb.append("\n");
      t++;
    }
    System.out.print(sb.toString());
  }
}
