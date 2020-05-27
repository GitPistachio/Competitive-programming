/*
* Project name : SPOJ: FANCY - FANCY NUMBERS
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-04-04
* Description  :
* Status       : Accepted (23568807)
* Tags         : java, math, probability theory, combinatorics
* Comment      :
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;

final class FANCY{
  static final class Reader{
      final private int BUFFER_SIZE = 1 << 18;
      private DataInputStream dis;
      private byte[] buffer;
      private int bufferPointer, bytesRead;
      private boolean EOF = false;

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

      public void readLine(byte[] line) throws IOException {
            byte c;
            int cnt = 0;
            while ((c = read()) != -1){
                if (c == '\n')
                    break;
                line[cnt++] = c;
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

      public int nextSolve() throws IOException{
        int no_of_combinations = 1;
        byte p = read(), c;

        while ((c = read()) >= '0'){
          if (p == c)
            no_of_combinations = no_of_combinations << 1;
          else
            p = c;
        }

        return no_of_combinations;
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
    StringBuilder sb =  new StringBuilder();
    int T = r.nextUnsignedInt();

    while (T-- > 0){
      sb.append(r.nextSolve());
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
