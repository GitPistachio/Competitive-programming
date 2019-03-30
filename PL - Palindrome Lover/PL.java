/*
* Project name : SPOJ: PL - Palindrome Lover
* Author       : Wojciech Raszka
* Date created : 2019-03-23
* Description  :
* Status       : Accepted (23477502)
* Tags         : java, fast I/O, string pattern, palindrome
* Comment      : O(n) where n is the length of given string
*/

import java.io.DataInputStream;
import java.io.IOException;

class PL{
  static final class Reader{
      final private int BUFFER_SIZE = 1 << 16;
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
      public byte readCharacter() throws IOException{
        byte c = read();
        while (c <= ' ')
            c = read();
        return c;
      }

      public void readLine(byte line[]) throws IOException {
        int cnt = 0;
        byte c;
        while ((c = read()) != -1){
            if (c == '\n'){
              line[cnt] = 0;
              break;
            }
            line[cnt++] = c;
        }
      }

      public int readNoOcc() throws IOException {
        byte c;
        int[] occ = new int[123];
        int no_of_chars = 0, no_of_odds = 0;

        while ((c = read()) != -1){
          if (c == '\n'){
            break;
          }
          occ[c]++;
        }

        for (int i = 97; i < 123 ; i++){
          if (occ[i] % 2 == 1){
            no_of_odds++;
          }
          if (occ[i] > 0){
            no_of_chars++;
          }
        }

        if (no_of_chars > 0){
          return no_of_odds;
        } else {
          return -1;
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
    int no_of_odds;

    do {
      no_of_odds = r.readNoOcc();
      if (no_of_odds < 0) break;

      if (no_of_odds > 1){
        System.out.println(-1);
      } else {
        System.out.println(1);
      }
    } while (true);

  }
}
