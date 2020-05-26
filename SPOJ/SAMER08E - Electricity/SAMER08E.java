/*
* Project name : SPOJ: SAMER08E - Electricity
* Author       : Wojciech Raszka
* Date created : 2019-03-20
* Description  :
* Status       : Accepted (23457260)
* Comment      :
*/

import java.io.DataInputStream;
import java.io.IOException;
import java.time.LocalDate;
import java.time.temporal.ChronoUnit;

class SAMER08E{
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
    int n, d, m, y, pc, c;
    int no_of_days, sum_of_consumption;
    LocalDate pld, ld;


    while ((n = r.nextUnsignedInt()) != 0){
      no_of_days = 0;
      sum_of_consumption = 0;

      d = r.nextUnsignedInt();
      m = r.nextUnsignedInt();
      y = r.nextUnsignedInt();
      pc = r.nextUnsignedInt();
      pld = LocalDate.of(y, m, d);

      while (n-- > 1){
        d = r.nextUnsignedInt();
        m = r.nextUnsignedInt();
        y = r.nextUnsignedInt();
        c = r.nextUnsignedInt();
        ld = LocalDate.of(y, m, d);

        if (ChronoUnit.DAYS.between(pld, ld) == 1){
          no_of_days++;
          sum_of_consumption += c - pc;
        }
        pld = ld;
        pc = c;
      }

      System.out.println(no_of_days + " " + sum_of_consumption);
    }
  }
}
