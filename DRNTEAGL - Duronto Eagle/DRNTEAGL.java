/*
* Project name : SPOJ: DRNTEAGL - Duronto Eagle
* Author       : Wojciech Raszka
* Date created : 2019-03-14
* Description  :
* Status       : Accepted (23406065)
* Comment      :
*/

import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;

class DRNTEAGL{
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
  public static int square_dist(int x1, int y1, int x2, int y2){
    return (x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2);
  }
  public static void main(String args[]) throws IOException{
    Reader r = new Reader();

    int T = r.nextInt();
    int n, x, y;
    int max_square_dist;
    int idx;
    int temp_square_dist;

    for (int t = 0; t < T; t++){
      n = r.nextInt();
      max_square_dist = 0;
      idx = 1;
      for (int i = 0; i < n; i++){
        x = r.nextInt();
        y = r.nextInt();
        temp_square_dist = square_dist(0, 0, x, y);
        if (temp_square_dist > max_square_dist){
            max_square_dist = temp_square_dist;
            idx = i + 1;
        }
      }
      System.out.println("Case " + (t + 1) + ": " + idx);
    }
  }
}
