/*
* Project name : SPOJ: SPCS - Gopu And Palindromes
* Author       : Wojciech Raszka
* Date created : 2019-03-20
* Description  :
* Status       : Accepted (23452000)
* Comment      :
*/

import java.io.DataInputStream;
import java.io.IOException;

class SPCS{
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

      public int readPalindrome(byte[] pln) throws IOException {
        byte c;
        int cnt = 0;

        if ((c = read()) != -1 && c != '\n'){
          pln[cnt++] = c;
        }

        while ((c = read()) != -1 && c != '\n'){
          if (pln[cnt - 1] != c){
              pln[cnt++] = c;
          }
        }
        return cnt;
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
    boolean is_palindrome;
    byte[] pln;
    int l;

    while (T-- > 0){
      is_palindrome = true;
      pln = new byte [100001];
      l = r.readPalindrome(pln);

      for (int i = 0, j = l - 1; i < j; i++, j--){
        if (pln[i] != pln[j]){
          is_palindrome = false;
          break;
        }
      }
      if (is_palindrome){
          System.out.println("YES");
      } else {
          System.out.println("NO");
      }
    }
  }
}
