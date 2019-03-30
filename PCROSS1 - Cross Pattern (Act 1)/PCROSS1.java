/*
* Project name : SPOJ: PCROSS1 - Cross Pattern (Act 1)
* Author       : Wojciech Raszka
* Date created : 2019-03-13
* Description  :
* Status       : Accepted (23403400)
* Comment      :
*/

import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;

class PCROSS1{
  static class Reader
    {
        final private int BUFFER_SIZE = 1 << 16;
        private DataInputStream dis;
        private byte[] buffer;
        private int bufferPointer, bytesRead;

        public Reader()
        {
            dis = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public Reader(String file_name) throws IOException
        {
            dis = new DataInputStream(new FileInputStream(file_name));
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public int nextInt() throws IOException
        {
            int ret = 0;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do
            {
                ret = ret * 10 + c - '0';
            }  while ((c = read()) >= '0' && c <= '9');

            if (neg)
                return -ret;
            return ret;
        }

        private void fillBuffer() throws IOException
        {
            bytesRead = dis.read(buffer, bufferPointer = 0, BUFFER_SIZE);
            if (bytesRead == -1)
                buffer[0] = -1;
        }

        private byte read() throws IOException
        {
            if (bufferPointer == bytesRead)
                fillBuffer();
            return buffer[bufferPointer++];
        }

        public void close() throws IOException
        {
            if (dis == null)
                return;
            dis.close();
        }
    }

  public static void drawCross(int m, int n, int c_i, int c_j){
    StringBuffer br = new StringBuffer(), loc = new StringBuffer(), cross = new StringBuffer();
    String brs;

    for (int j = 0; j < n; j++){
      if (j + 1 == c_j){
        br.append("*");
      } else {
        br.append(".");
      }
      loc.append("*");
    }
    br.append("\n");
    loc.append("\n");

    for (int i = 0; i < m; i++){
      if (i + 1 == c_i){
        cross.append(loc);
      } else{
        cross.append(br);
      }
    }
    System.out.print(cross.toString());
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    int T = r.nextInt();
    int m, n, c_i, c_j;

    for (int t = 0; t < T; t++){
      m = r.nextInt();
      n = r.nextInt();
      c_i = r.nextInt();
      c_j = r.nextInt();

      drawCross(m, n, c_i, c_j);
      System.out.print("\n");
    }
  }
}
