/*
* Project name : SPOJ: STACKEZ - Easy Stack
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-04-25
* Description  :
* Status       : Accepted (23685754)
* Tags         : java, fast I/O, stack
* Comment      :
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;
import java.util.Stack;

final class STACKEZ{
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
    StringBuilder sb = new StringBuilder();
    Stack<Integer> st = new Stack<Integer>();
    int no_of_operations = r.nextUnsignedInt();
    int t;
    int n;

    while (no_of_operations-- > 0){
      t = r.nextUnsignedInt();

      if (t == 1){
        n = r.nextUnsignedInt();
        st.push(n);
      } else if (t == 2){
        if (!st.empty()){
            st.pop();
        }
      } else {
        if (st.empty()){
          sb.append("Empty!\n");
        } else {
          sb.append(st.peek());
          sb.append('\n');
        }
      }
    }
    System.out.print(sb.toString());
  }
}
