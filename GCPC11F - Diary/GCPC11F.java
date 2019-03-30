/*
* Project name : SPOJ: GCPC11F - Diary
* Author       : Wojciech Raszka
* Date created : 2019-03-19
* Description  :
* Status       : Accepted (23450239)
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
    byte[] entry;
    int i, key, d, t;
    int[] alphabet;
    boolean is_possible;

    while (T-- > 0){
      entry = new byte[1001];
      alphabet = new int [26];

      r.readLine(entry);

      d = -1;
      i = 0;
      is_possible = true;
      while (entry[i] != 0){
        if (entry[i] >= 'A' && entry[i] <= 'Z'){
          t = entry[i] - 'A';
          alphabet[t]++;

          if (d < 0){
            d = t;
          } else if (alphabet[t] > alphabet[d] || t == d){
            d = t;
            is_possible = true;
          } else if (t != d && alphabet[t] == alphabet[d]){
            is_possible = false;
          }
        }
        i++;
      }

      key = (30 - d) % 26;
      i = 0;
      while (entry[i] != 0){
        if (entry[i] >= 'A' && entry[i] <= 'Z'){
          entry[i] = (byte) (65 + (entry[i] - 65 + key) % 26);
        }
        i++;
      }

      if (is_possible){
        System.out.println((26 - key) % 26 + " " + (new String(entry, 0, i)));
      } else {
        System.out.println("NOT POSSIBLE");
      }
    }
  }
}
