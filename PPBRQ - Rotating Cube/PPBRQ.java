/*
* Project name : SPOJ: PPBRQ - Rotating Cube
* Author       : Wojciech Raszka
* Date created : 2019-03-24
* Description  :
* Status       : Accepted (23482838)
* Tags         : java, fast I/O, cube rotation
* Comment      :
*/

import java.io.DataInputStream;
import java.io.IOException;

final class PPBRQ{
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

      public String nextWord() throws IOException{
        byte[] buf = new byte[15];
        int cnt = 0;
        byte c = read();

        while (c <= ' ')
            c = read();
        do{
            buf[cnt++] = c;
        } while ((c = read()) != -1 && c > ' ');

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
  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    int T = r.nextUnsignedInt();
    String[] initial_words = new String[6];
    int n, m, front, top, bottom, left, right, rear;
    int side;
    byte type_of_rotation;


    while (T-- > 0){
      front = 0; top = 1; bottom = 2; left = 3; right = 4; rear = 5;
      for (int i = 0; i < 6; i++){
        initial_words[i] = r.nextWord();
      }
      n = r.nextUnsignedInt();

      while (n-- > 0){
        type_of_rotation = r.read();
        m = r.nextUnsignedInt() % 4;
        switch (type_of_rotation){
          case 'X':
            switch (m){
              case 1:
                side = top;
                top = front; front = bottom; bottom = rear; rear = side;
                break;
              case 2:
                side = top;
                top = bottom; bottom = side;
                side = front;
                front = rear; rear = side;
                break;
              case 3:
                side = top;
                top = rear; rear = bottom; bottom = front; front = side;
                break;
            }
            break;
          case 'Y':
            switch (m){
              case 1:
                side = top;
                top = left; left = bottom; bottom = right; right = side;
                break;
              case 2:
                side = top;
                top = bottom; bottom = side;
                side = right;
                right = left; left = side;
                break;
              case 3:
                side = top;
                top = right; right = bottom; bottom = left; left = side;
                break;
            }
            break;
          case 'Z':
            switch (m){
              case 1:
                side = right;
                right = front; front = left; left = rear; rear = side;
                break;
              case 2:
                side = right;
                right = left; left = side;
                side = front;
                front = rear; rear = side;
                break;
              case 3:
                side = right;
                right = rear; rear = left; left = front; front = side;
                break;
            }
            break;
        }
      }

      System.out.println(initial_words[front] + " " + initial_words[top] + " " + initial_words[bottom] + " " + initial_words[left] + " " + initial_words[right] + " " + initial_words[rear]);
    }
  }
}
