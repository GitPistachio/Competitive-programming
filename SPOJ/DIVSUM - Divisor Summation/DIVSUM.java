/*
* Project name : SPOJ: DIVSUM - Divisor Summation
* Author       : Wojciech Raszka
* Date created : 2019-04-06
* Description  :
* Status       : Accepted (23586201)
* Tags         : java, fast I/O, number theory, divisor summation, number factorization
* Comment      :
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;
import java.lang.Math;

class DIVSUM{
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

  public static int sumOfDivisors(int n){
    int sum_of_divisors = 1;
    int sum_of_terms, term;

    for (int i = 2; i <= Math.sqrt(n); i++){
      sum_of_terms = 1;
      term = 1;
      while (n % i == 0){
        n /= i;
        term *= i;
        sum_of_terms += term;
      }
      sum_of_divisors *= sum_of_terms;
    }

    if (n > 1){
      sum_of_divisors *= (1 + n);
    }

    return sum_of_divisors;
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    int n, T = r.nextUnsignedInt();

    while (T-- > 0){
      n = r.nextUnsignedInt();
      sb.append(sumOfDivisors(n) - n);
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
