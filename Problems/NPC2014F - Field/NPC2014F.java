/*
* Project name : SPOJ: NPC2014F - Field
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-03-22
* Description  :
* Status       : Accepted (23470521)
* Tags         : java, fast I/O, string pattern, sliding window
* Comment      :
*/

import java.io.DataInputStream;
import java.io.IOException;

class NPC2014F{
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
    int N = r.nextUnsignedInt(), K;
    int[] tax_pattern = new int[26];
    boolean[] is_required = new boolean[26];
    int c, x, remaining_tax = 0, min_loss;

    byte[] field = new byte[N];

    r.readLine(field);
    K = r.nextUnsignedInt();

    for (int i = 0; i < K; i++){
      x = r.nextUnsignedInt();
      remaining_tax += x;
      c = r.readCharacter() - 'a';
      tax_pattern[c] = x;
      is_required[c] = true;
    }

    min_loss = N + 1;
    int s = 0, i = 0;
    while (i < N){
      if (is_required[field[i] - 'a']){
        if (tax_pattern[field[i] - 'a'] > 0){
            remaining_tax--;
        }
        tax_pattern[field[i] - 'a']--;
      }

      if (remaining_tax == 0){

        while (s <= i){
          if (is_required[field[s] - 'a']){
            tax_pattern[field[s] - 'a']++;
            if (tax_pattern[field[s] - 'a'] > 0){
              remaining_tax++;
              s++;
              break;
            }
          }
          s++;
        }
        if (i - s + 2 < min_loss){
          min_loss = i - s + 2;
        }
      }
      i++;
    }
    if (min_loss <= N){
      System.out.println(min_loss);
    } else{
      System.out.println("Andy rapopo");
    }
  }
}
