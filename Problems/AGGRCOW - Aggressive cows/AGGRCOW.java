/*
* Project name : SPOJ: AGGRCOW - Aggressive cows
* Author       : Wojciech Raszka
* Email        : gitpistachio@gmail.com
* Date created : 2019-04-17
* Description  :
* Status       : Accepted (23650441)
* Tags         : java, fast I/O, discrete binary search
* Comment      :
*/

import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;

final class AGGRCOW{
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

  static int[] A;

  public static boolean p(int d, int no_of_stalls, int no_of_cows){
    int last_cow_stall_position = A[0];
    int no_of_placed_cows = 1;

    for (int i = 1; i < no_of_stalls; i++){
      if (A[i] - last_cow_stall_position >= d){
        last_cow_stall_position = A[i];
        no_of_placed_cows++;
        if (no_of_placed_cows >= no_of_cows) return true;
      }
    }

    return false;
  }

  public static int binary_search(int l, int r, int no_of_stalls, int no_of_cows){
    int d;
    while (l < r){
      d = l + (r - l + 1)/2;
      if (p(d, no_of_stalls, no_of_cows)){
        l = d;
      } else{
        r = d - 1;
      }
    }
    return l;
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();

    int T = r.nextUnsignedInt(), no_of_stalls, no_of_cows;

    while (T-- > 0){
      no_of_stalls = r.nextUnsignedInt();
      no_of_cows = r.nextUnsignedInt();
      A = new int[no_of_stalls];

      for(int i = 0; i < no_of_stalls; i++){
        A[i] = r.nextUnsignedInt();
      }

      Arrays.sort(A);

      System.out.println(binary_search(0, A[no_of_stalls - 1] - A[0], no_of_stalls, no_of_cows));
    }
  }
}
