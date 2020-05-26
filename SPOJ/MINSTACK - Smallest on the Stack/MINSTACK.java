/*
* Project name : SPOJ: MINSTACK - Smallest on the Stack
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-16
* Description  :
* Status       : Accepted (23927595)
* Tags         : java, fast I/O, stack, minimal value on stack
* Comment      :
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;
import java.util.Stack;

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

  public String nextWord() throws IOException {
    byte[] buf = new byte[10];
    int cnt = 0;
    byte c = read();

    while (c <= ' ')
      c = read();

    buf[cnt++] = c;
    while ((c = read()) != -1) {
      if (c <= ' ') {
        break;
      }

      buf[cnt++] = c;
    }
    return new String(buf, 0, cnt);
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

final class MINSTACK{
  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    Stack<Integer> st = new Stack<Integer>();
    int n = r.nextPositiveInt(), val;
    String type_of_operation;


    while (n-- > 0){
      type_of_operation = r.nextWord();
      if (type_of_operation.charAt(1) == 'U'){
        val = r.nextPositiveInt();
        if (st.isEmpty()){
          st.push(val);
        } else {
          if (st.peek() > val) {
            st.push(val);
          } else {
            st.push(st.peek());
          }
        }

      } else if (type_of_operation.charAt(1) == 'O'){
        if (st.isEmpty()) {
          sb.append("EMPTY\n");
        } else {
          st.pop();
        }
      } else {
        if (st.isEmpty()) {
          sb.append("EMPTY\n");
        } else {
          sb.append(st.peek());
          sb.append('\n');
        }
      }
    }
    System.out.print(sb.toString());
  }
}
