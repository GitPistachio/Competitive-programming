/*
* Project name : SPOJ: ABCDEF - ABCDEF
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-10
* Description  :
* Status       : Accepted (23902787)
* Tags         : java, Fast I/O, map, linear Diophantine equation
* Comment      :
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;
import java.util.Map;
import java.util.HashMap;

final class Reader{
  final private int BUFFER_SIZE = 1 << 16;
  private DataInputStream dis;
  private byte[] buffer, token;
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
    int no_of_sextuples = 0, val, g, h, m, n = r.nextPositiveInt(), n3 = n*n*(n + 1)/2;
    int[] A = new int[n];
    int[] T = new int[n3];
    boolean[] is_single = new boolean[n3];
    Integer no_of_triples;
    Map<Integer, Integer> triplets = new HashMap<Integer, Integer>();

    for (int i = 0; i < n; i++){
      A[i] = r.nextInt();
    }

    m = 0;
    for (int i = 0; i < n; i++){
      g = A[i]*A[i];
      h = A[i] + A[i];
      for (int k = 0; k < n; k++){
        if (A[k] != 0){
          is_single[m] = true;
          T[m++] = h*A[k];
        }
        val = g + A[k];
        no_of_triples = triplets.get(val);
        if (no_of_triples == null){
          triplets.put(val, 1);
        } else {
          triplets.put(val, no_of_triples + 1);
        }
      }

      for (int j = i + 1; j < n; j++){
        g = A[i]*A[j];
        h = A[i] + A[j];
        for (int k = 0; k < n; k++){
          if (A[k] != 0){
            T[m++] = h*A[k];
          }
          val = g + A[k];
          no_of_triples = triplets.get(val);
          if (no_of_triples == null){
            triplets.put(val, 2);
          } else {
            triplets.put(val, no_of_triples + 2);
          }
        }
      }
    }

    for (int i = 0; i < m; i++){
      no_of_triples = triplets.get(T[i]);
      if (no_of_triples != null){
        if (is_single[i]){
          no_of_sextuples += no_of_triples;
        } else {
          no_of_sextuples += no_of_triples << 1;
        }
      }
    }
    System.out.println(no_of_sextuples);
  }
}
