/*
* Project name : SPOJ: BTCODE_F - Life Game
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-03-21
* Description  :
* Status       : Accepted (23463266)
* Tags         : java, fast I/O, game theory, optimized brute force, dynamic-programming
* Comment      :
*/

import java.io.DataInputStream;
import java.io.IOException;

class BTCODE_F{
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

  public static void find_results(int r, int c, int score, int M, int N, int[][] board, boolean[][][] reached_scores){
    if (!reached_scores[r][c][score + 625]){
      reached_scores[r][c][score + 625] = true;
      if (r < M - 1){
        find_results(r + 1, c, score + board[r + 1][c], M, N, board, reached_scores);

        if (c > 0){
          find_results(r + 1, c - 1, score + board[r + 1][c - 1], M, N, board, reached_scores);
        }
        if (c < N - 1){
          find_results(r + 1, c + 1, score + board[r + 1][c + 1], M, N, board, reached_scores);
        }
      }
    }
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    int T = r.nextUnsignedInt();
    int M, N, A, B;
    final int HALF_OF_NO_OF_POSSIBLE_SCORES = 25*25;
    int[][] board;
    boolean[][][] reached_scores;

    while (T-- > 0){
      M = r.nextUnsignedInt();
      N = r.nextUnsignedInt();
      A = r.nextInt();
      B = r.nextInt();

      if (A < -HALF_OF_NO_OF_POSSIBLE_SCORES){
        A = -HALF_OF_NO_OF_POSSIBLE_SCORES;
      } else if (A > HALF_OF_NO_OF_POSSIBLE_SCORES){
        A = HALF_OF_NO_OF_POSSIBLE_SCORES;
      }

      if (B < -HALF_OF_NO_OF_POSSIBLE_SCORES){
        B = -HALF_OF_NO_OF_POSSIBLE_SCORES;
      } else if (B > HALF_OF_NO_OF_POSSIBLE_SCORES){
        B = HALF_OF_NO_OF_POSSIBLE_SCORES;
      }

      board = new int[M][N];
      reached_scores = new boolean[M][N][2*HALF_OF_NO_OF_POSSIBLE_SCORES + 1];

      for (int i = 0; i < M; i++){
        for (int j = 0; j < N; j++){
          board[i][j] = r.nextInt();
        }
      }

      for (int j = 0; j < N; j++){
          find_results(0, j, board[0][j], M, N, board, reached_scores);
      }

      int Hmin = HALF_OF_NO_OF_POSSIBLE_SCORES + 1, Hmax = -HALF_OF_NO_OF_POSSIBLE_SCORES - 1;
      for (int j = 0; j < N; j++){
        for (int score = A;  score <= B; score++){
          if (reached_scores[M - 1][j][score + HALF_OF_NO_OF_POSSIBLE_SCORES]){
            if (Hmin > score){
              Hmin = score;
            }
            if (Hmax < score){
                Hmax = score;
            }
          }
        }
      }
      if (Hmin <= HALF_OF_NO_OF_POSSIBLE_SCORES && Hmax >= -HALF_OF_NO_OF_POSSIBLE_SCORES){
        System.out.println(Hmin + " " + Hmax);
      } else if (Hmin > HALF_OF_NO_OF_POSSIBLE_SCORES && Hmax >= -HALF_OF_NO_OF_POSSIBLE_SCORES){
        System.out.println("NO " + Hmax);
      } else if (Hmin <= HALF_OF_NO_OF_POSSIBLE_SCORES && Hmax < -HALF_OF_NO_OF_POSSIBLE_SCORES){
        System.out.println(Hmin + " NO");
      } else{
        System.out.println("NO NO");
      }
    }
  }
}
