/*
* Project name : SPOJ: DCRYPT - Decrypt the message !
* Author       : Wojciech Raszka
* Date created : 2019-03-18
* Description  :
* Status       : Accepted (23442132)
* Comment      :
*/

import java.io.DataInputStream;
import java.io.IOException;

class DCRYPT{
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
    int i, key, offset;
    byte[] msg;

    while (T-- > 0){
      key = r.nextUnsignedInt();
      msg = new byte[100001];
      r.readLine(msg);
      i = 0;
      while (msg[i] != 0){
        if (msg[i] == '.'){
          msg[i] = ' ';
        } else{
          offset = key % 26;
          if (msg[i] >= 'a' && msg[i] <= 'z'){
            msg[i] = (byte) (97 + (msg[i] - 97 + offset) % 26);
          } else if (msg[i] >= 'A' && msg[i] <= 'Z'){
            msg[i] = (byte) (65 + (msg[i] - 65 + offset) % 26);
          }
          if (key >= 26){
            if (msg[i] >= 'a')
              msg[i] -= 32;
            else{
              msg[i] += 32;
            }
          }
        }
        i++;
      }
      System.out.println(new String(msg, 0, i));
    }
  }
}
