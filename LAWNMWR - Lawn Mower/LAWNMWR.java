/*
* Project name : SPOJ: LAWNMWR - Lawn Mowe
* Author       : Wojciech Raszka
* Date created : 2019-02-22
* Description  :
* Status       : Accepted (23281990)
* Comment      :
*/

import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.Arrays;

class LAWNMWR{
  static class Reader
    {
        final private int BUFFER_SIZE = 1 << 16;
        private DataInputStream din;
        private byte[] buffer;
        private int bufferPointer, bytesRead;

        public Reader()
        {
            din = new DataInputStream(System.in);
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public Reader(String file_name) throws IOException
        {
            din = new DataInputStream(new FileInputStream(file_name));
            buffer = new byte[BUFFER_SIZE];
            bufferPointer = bytesRead = 0;
        }

        public String readLine() throws IOException
        {
            byte[] buf = new byte[11000]; // line length
            int cnt = 0, c;
            while ((c = read()) != -1)
            {
                if (c == '\n')
                    break;
                buf[cnt++] = (byte) c;
            }
            return new String(buf, 0, cnt);
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

        public long nextLong() throws IOException
        {
            long ret = 0;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();
            do {
                ret = ret * 10 + c - '0';
            }
            while ((c = read()) >= '0' && c <= '9');
            if (neg)
                return -ret;
            return ret;
        }

        public float nextFloat() throws IOException
        {
            float ret = 0, div = 1;
            byte c = read();
            while (c <= ' ')
                c = read();
            boolean neg = (c == '-');
            if (neg)
                c = read();

            do {
                ret = ret * 10 + c - '0';
            }
            while ((c = read()) >= '0' && c <= '9');

            if (c == '.')
            {
                while ((c = read()) >= '0' && c <= '9')
                {
                    ret += (c - '0') / (div *= 10);
                }
            }

            if (neg)
                return -ret;
            return ret;
        }

        private void fillBuffer() throws IOException
        {
            bytesRead = din.read(buffer, bufferPointer = 0, BUFFER_SIZE);
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
            if (din == null)
                return;
            din.close();
        }
    }

  static boolean check(float X[], int n, float L, float w){
    if (X[0] > w/2 || L - X[n - 1] > w/2) return false;
    for (int i = 1; i < n; i++){
      if (X[i] - X[i - 1] > w) return false;
    }
    return true;
  }
  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    int n_x, n_y;
    float w;
    float[] X, Y;
    boolean yes_no;
    final float field_length = 100;
    final float field_width = 75;

    n_x = r.nextInt();
    n_y = r.nextInt();
    w = r.nextFloat();
    while (w > 0){
      if (n_x*w < field_width || n_y*w < field_length){
        System.out.println("NO");
        r.readLine();
        r.readLine();
      } else {
        yes_no = true;
        X = new float[n_x];
        for (int i = 0; i < n_x; i++){
          X[i] = r.nextFloat();
        }
        Arrays.sort(X);
        if (!check(X, n_x, field_width, w)){
          System.out.println("NO");
          r.readLine();
          yes_no = false;
        }

        if (yes_no){
          Y = new float[n_y];
          for (int i = 0; i < n_y; i++){
            Y[i] = r.nextFloat();
          }

          Arrays.sort(Y);
          if (check(Y, n_y, field_length, w)){
            System.out.println("YES");
          } else {
            System.out.println("NO");
          }
        }
      }
      n_x = r.nextInt();
      n_y = r.nextInt();
      w = r.nextFloat();
    }
  }
}
