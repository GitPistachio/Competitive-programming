/*
* Project name : SPOJ: KLUG1 - COUNT JUMPS
* Author       : Wojciech Raszka
* Date created : 2019-03-09
* Description  :
* Status       : Accepted (23373700)
* Comment      :
*/

import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;

class KLUG1{
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

  public static boolean isPossible(int i, int j, int n, int m, boolean chessboard[][]){
    if (i >= 0 && j >= 0 && i < n && j < m){
      if (!chessboard[i][j]){
          return true;
      } else{
          return false;
      }
    }
    return false;
  }
  public static void main(String args[]) throws IOException{
    Reader r = new Reader();

    int n = r.nextInt(), m = r.nextInt();
    int a, b;
    int no_of_possible_movements = 0;
    boolean[][] chessboard = new boolean[n][m];

    for (int i = 0; i < n; i++){
      for (int j = 0; j < m; j++){
        if (r.nextInt() == 1){
            chessboard[i][j] = true;
        }
      }
    }

    a = r.nextInt() - 1;
    b = r.nextInt() - 1;

    if (isPossible(a - 2, b - 1, n, m, chessboard)) no_of_possible_movements++;
    if (isPossible(a - 2, b + 1, n, m, chessboard)) no_of_possible_movements++;
    if (isPossible(a + 2, b - 1, n, m, chessboard)) no_of_possible_movements++;
    if (isPossible(a + 2, b + 1, n, m, chessboard)) no_of_possible_movements++;
    if (isPossible(a - 1, b - 2, n, m, chessboard)) no_of_possible_movements++;
    if (isPossible(a + 1, b - 2, n, m, chessboard)) no_of_possible_movements++;
    if (isPossible(a - 1, b + 2, n, m, chessboard)) no_of_possible_movements++;
    if (isPossible(a + 1, b + 2, n, m, chessboard)) no_of_possible_movements++;

    System.out.println(no_of_possible_movements);
  }
}
