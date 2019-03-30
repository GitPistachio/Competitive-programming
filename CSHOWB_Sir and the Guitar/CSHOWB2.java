/*
* Project name : SPOJ: CSHOWB - Sir and the Guitar
* Author       : Wojciech Raszka
* Date created : 2019-03-08
* Description  :
* Status       : Accepted (23385950)
* Comment      :
*/

import java.io.DataInputStream;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.SortedSet;
import java.util.TreeSet;
import java.util.ArrayList;


class CSHOWB2{
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

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();

    int N = r.nextInt(), P = r.nextInt();
    ArrayList<SortedSet<Integer>> G = new ArrayList<SortedSet<Integer>>();
    for (int i = 0; i < 6; i++){
      G.add(new TreeSet<Integer>());
    }
    int s, f;
    int no_of_finger_movements = 0;

    for(int i = 0; i < N; i++){
      s = r.nextInt() - 1;
      f = r.nextInt();

      if (G.get(s).isEmpty()){
        G.get(s).add(f);
        no_of_finger_movements++;
      } else if (G.get(s).last() < f){
        G.get(s).add(f);
        no_of_finger_movements++;
      } else if (G.get(s).last() > f){
        no_of_finger_movements += G.get(s).tailSet(f + 1).size();
        if (!G.get(s).contains(f)){
          G.get(s).add(f);
          no_of_finger_movements++;
        }
        G.get(s).tailSet(f + 1).clear();
      }
    }
    System.out.println(no_of_finger_movements);
  }
}
