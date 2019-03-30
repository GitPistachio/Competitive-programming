/*
* Project name : SPOJ: BAISED - Biased Standings
* Author       : Wojciech Raszka
* Date created : 2019-03-17
* Description  :
* Status       : Accepted (23432762)
* Comment      : O(n) 
*/

import java.io.DataInputStream;
import java.io.IOException;

class BAISED{
  static class Reader{
      final private int BUFFER_SIZE = 1 << 23;
      private DataInputStream dis;
      private byte[] buffer;
      private int bufferPointer, bytesRead;

      public Reader(){
          dis = new DataInputStream(System.in);
          buffer = new byte[BUFFER_SIZE];
          bufferPointer = bytesRead = 0;
      }

      public void omitWord() throws IOException {
        byte c;
        while (read() <= ' ');
        while ((c = read()) != -1){
              if (c == ' ')
                  break;
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
    int n;
    long badness, position;
    long[] prefered_position;

    while(T-- > 0){
      n = r.nextUnsignedInt();
      prefered_position = new long[n + 1];
      for (int i = 0; i < n; i++){
        r.omitWord();
        prefered_position[r.nextUnsignedInt()]++;
      }
      badness = 0;
      position = 1;
      for (int i = 1; i <= n; i++){
        if (i <= position){
          badness += (prefered_position[i] - 1)*prefered_position[i]/2 + prefered_position[i]*(position - i);
        } else if (position + prefered_position[i] - 1 <= i){
          badness += (prefered_position[i] - 1)*prefered_position[i]/2 + prefered_position[i]*(i - position - prefered_position[i] + 1);
        } else{
          badness += ((i - position)*(i - position + 1) + (position + prefered_position[i] - i - 1)*(position + prefered_position[i] - i))/2;
        }

        position += prefered_position[i];
      }
      System.out.println(badness);
    }
  }
}
