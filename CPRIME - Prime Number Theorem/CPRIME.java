/*
* Project name : SPOJ: CPRIME - Prime Number Theorem
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-02
* Description  :
* Status       : Accepted (23866151)
* Tags         ; java, fast I/O, prime number theorem, math, number theorem, prime numbers, pi function, sieve of erathotestenes, 2-3-5 wheel factorization
* Comment      :
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;
import java.lang.Math;

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

final class CPRIME{
  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    int x;

    final int MAX_N = 100000000;
    boolean[] is_not_prime = new boolean[MAX_N + 1];
    int p;
    int[] wheel = {6,4,2,4,2,4,6,2};
    int[] primes = {7,11,13,17,19,23,29,31};
    int[] first_primes = {2,3,5,7,11,13,17,19,23,29,31};
    int[] no_of_primes = new int[MAX_N + 1];
    boolean run;
    double err;

    run = true;
    for (int k:primes){
	    for (int i = k*k; i <= MAX_N; i += k){
			is_not_prime[i] = true;
		  }
    }

    p = 31;
    while (run){
      for (int w:wheel){
        p += w;
        if (p*p > MAX_N) {
          run = false;
          break;
        }
        if (is_not_prime[p] == false){
          for (int i = p*p; i <= MAX_N; i += p){
            is_not_prime[i] = true;
          }
        }
      }
    }

    p = 1;
    for (int k:first_primes){
      for (int i = p + 1; i < k; i++){
        no_of_primes[i] = no_of_primes[i - 1];
      }
      no_of_primes[k] = no_of_primes[k - 1] + 1;
      p = k;
    }

    run = true;
    p = 31;
    while (run){
      for (int w:wheel){
        p += w;
        if (p > MAX_N) {
          run = false;
          for (int i = p - w + 1; i <= MAX_N; i++){
            no_of_primes[i] = no_of_primes[i - 1];
          }
          break;
        }
        for (int i = p - w + 1; i < p; i++){
          no_of_primes[i] = no_of_primes[i - 1];
        }

        if (is_not_prime[p] == false){
          no_of_primes[p] = no_of_primes[p - 1] + 1;
        } else {
          no_of_primes[p] = no_of_primes[p - 1];
        }
      }
    }

    while ((x = r.nextPositiveInt()) != 0){
      err = Math.abs(no_of_primes[x] - x/Math.log(x))/no_of_primes[x];
      sb.append(Math.round(err*1000)/10.0);
      sb.append('\n');
    }

    System.out.print(sb.toString());
  }
}
