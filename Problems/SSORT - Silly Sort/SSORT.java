/*
* Project name : SPOJ: SSORT - Silly Sort
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-04
* Description  :
* Status       : Accepted (23878898)
* Tags         : java, fast I/O, sorting, minimal cost sorting
* Comment      :
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;
import java.util.Map;
import java.util.HashMap;

final class Reader{
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

  public String nextWord() throws IOException{
    byte[] buf = new byte[30];
    int cnt = 0;
    byte c;
    while ((c = read()) != -1){
      if (c <= ' '){
        if (cnt > 0){
          break;
        }
      } else {
        buf[cnt++] = c;
      }
    }

    return new String(buf, 0, cnt);
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

  public long nextPositiveLong() throws IOException{
      long ret = 0;
      byte c = read();
      while (c <= ' ')
          c = read();
      do{
          ret = ret * 10 + c - '0';
      }  while ((c = read()) >= '0' && c <= '9');

      return ret;
  }

  public int nextPositiveInt() throws IOException{
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

final class VFMUL{
  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    final int MAX_SIZE = 50000;
    int j, t, n, min_a_in_cycle, cost_of_cycle, total_cost, len_of_cycle;
    int[] A = new int[MAX_SIZE];
    int[] B = new int[MAX_SIZE];
    Map<Integer, Integer> placement = new HashMap<Integer, Integer>();
    boolean[] visited = new boolean[MAX_SIZE];

    t = 1;

    while ((n = r.nextPositiveInt()) != 0){
      for (int i = 0; i < n; i++){
        A[i] = r.nextPositiveInt();
        B[i] = A[i];
      }

      Arrays.sort(B, 0, n);

      for (int i = 0; i < n; i++){
        placement.put(B[i], i);
        visited[i] = false;
      }

      total_cost = 0;
      for (int i = 0; i < n; i++){
        if (visited[i] || placement.get(A[i]) == i) continue;

        min_a_in_cycle = A[i];
        cost_of_cycle = A[i];
        len_of_cycle = 1;
        j = placement.get(A[i]);
        visited[i] = true;

        while (visited[j] == false){
          cost_of_cycle += A[j];
          visited[j] = true;
          if (A[j] < min_a_in_cycle){
            min_a_in_cycle = A[j];
          }
          j = placement.get(A[j]);
          len_of_cycle++;
        }


        if (2*(B[0] + min_a_in_cycle) < (min_a_in_cycle - B[0])*(len_of_cycle - 1)){
          cost_of_cycle += min_a_in_cycle + B[0]*(len_of_cycle + 1);
        } else {
          cost_of_cycle += min_a_in_cycle*(len_of_cycle - 2);
        }
        total_cost += cost_of_cycle;
      }

      sb.append("Case ");
      sb.append(t);
      sb.append(": ");
      sb.append(total_cost);
      sb.append("\n\n");
      t++;

      placement.clear();
    }
    System.out.print(sb.toString());
  }
}
