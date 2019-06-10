/*
* Project name : SPOJ: POLYMUL - Polynomial Multiplication
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-07
* Description  :
* Status       : Accepted (23890615)
* Tags         : java, fast I/O, FFT, fast Fourier transform, polynomial multiplication, bit reverse, logarithm base two
* Comment      :
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;
import java.lang.Math;

final class Reader{
  final private int BUFFER_SIZE = 1 << 16;
  private DataInputStream dis;
  private byte[] buffer, token;
  private int bufferPointer, bytesRead;

  public Reader(){
      dis = new DataInputStream(System.in);
      buffer = new byte[BUFFER_SIZE];
      token = new byte[300000];
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

final class POLYMUL{
  public static double lg(double x){
    return Math.log(x)/Math.log(2);
  }

  public static int bitReverse(int n, int no_of_bits) {
    int reversed_n = n;
    int count = no_of_bits - 1;

    n >>= 1;
    while (n > 0){
      reversed_n = (reversed_n << 1) | (n & 1);
      count--;
      n >>= 1;
    }

    return ((reversed_n << count) & ((1 << no_of_bits) - 1));
    }

  public static void fft(double X0[], double X1[], double x[], int x_len, int n){
    double dpi = -6.283185307179586476925286766559;
    int L = 1, L2, r, l = n/2, m = l - x_len;
    int no_of_bits = (int) lg(n);
    double c, w0, w1, e0, e1;
    double u0, v0, u1, v1;
    int reversed_i;
    int even_idx, odd_idx;

    for (int i = 0; i < n; i++){
        reversed_i = bitReverse(i, no_of_bits);

        if(reversed_i < l && reversed_i >= m){
          X0[i] = x[reversed_i - m];  X1[i] = 0;
        } else {
          X0[i] = 0; X1[i] = 0;
        }
    }

    for (int q = 1; q <= no_of_bits; q++){
      L2 = L;
      L = 2*L;
      r = n/L;
      w0 = 1; w1 = 0;

      e0 = Math.cos(dpi/L); e1 = Math.sin(dpi/L);

      for (int j = 0; j <= L2 - 1; j++){
        for (int k = 0; k <= r - 1; k++){
          even_idx = k*L + j;
          odd_idx = even_idx + L2;

          u0 = X0[even_idx]; u1 = X1[even_idx];
          v0 = w0*X0[odd_idx] - w1*X1[odd_idx]; v1 = w0*X1[odd_idx] + w1*X0[odd_idx];

          X0[even_idx] = u0 + v0; X1[even_idx] = u1 + v1;
          X0[odd_idx] = u0 - v0; X1[odd_idx] = u1 - v1;
        }

        c = e0*w0 - e1*w1;
        w1 = e0*w1 + e1*w0;
        w0 = c;
      }
    }
  }

  public static void ifft(double X0[], double X1[], double x0[], double x1[], int n){
    double dpi = 6.283185307179586476925286766559;
    int L = 1, L2, r;
    int no_of_bits = (int) lg(n);
    double c, w0, w1, e0, e1;
    double u0, v0, u1, v1;
    int reversed_i;
    int even_idx, odd_idx;

    for (int i = 0; i < n; i++){
        reversed_i = bitReverse(i, no_of_bits);

        X0[i] = x0[reversed_i];  X1[i] = x1[reversed_i];
    }

    for (int q = 1; q <= no_of_bits; q++){
      L2 = L;
      L = 2*L;
      r = n/L;
      w0 = 1; w1 = 0;

      e0 = Math.cos(dpi/L); e1 = Math.sin(dpi/L);

      for (int j = 0; j <= L2 - 1; j++){
        for (int k = 0; k <= r - 1; k++){
          even_idx = k*L + j;
          odd_idx = even_idx + L2;

          u0 = X0[even_idx]; u1 = X1[even_idx];
          v0 = w0*X0[odd_idx] - w1*X1[odd_idx]; v1 = w0*X1[odd_idx] + w1*X0[odd_idx];

          X0[even_idx] = u0 + v0; X1[even_idx] = u1 + v1;
          X0[odd_idx] = u0 - v0; X1[odd_idx] = u1 - v1;
        }

        c = e0*w0 - e1*w1;
        w1 = e0*w1 + e1*w0;
        w0 = c;
      }
    }
  }

  public static int findFirstPowerOf2GreaterThanN(int N){
    int n = 2;

    while (n < 2*N){
      n = n << 1;
    }

    return n;
  }

  public static int max(int x, int y){
    if (x > y){
      return x;
    } else {
      return y;
    }
  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    int T = r.nextPositiveInt();
    final int MAX_NO_OF_DIGITS = 10001;
    final int MAX_N = 32769;

    double[] x = new double[MAX_NO_OF_DIGITS];
    double[] y = new double[MAX_NO_OF_DIGITS];
    long[] result = new long[MAX_N];
    int m, n, stop, max_len, k;
    long remainder, value, pass_over_value;
    double dpi = 6.283185307179586476925286766559, stop_cond;
    double[] X0 = new double[MAX_N], X1 = new double[MAX_N];
    double[] Y0 = new double[MAX_N], Y1 = new double[MAX_N];
    double[] Z0 = new double[MAX_N], Z1 = new double[MAX_N];
    double[] z0 = new double[MAX_N], z1 = new double[MAX_N];

    k = 0;
    while (T-- > 0){
      m = r.nextPositiveInt() + 1;
      n = findFirstPowerOf2GreaterThanN(m);

      for (int i = m - 1; i >= 0; i--){
        x[i] = r.nextInt();
      }

      for (int i = m - 1; i >= 0; i--){
        y[i] = r.nextInt();
      }

      if (m == 1){
        sb.append(Math.round(x[0]*y[0]));
      } else {

        //Stage 1, calculation of FFT of both numbers written as polymonials
        fft(X0, X1, x, m, n);
        fft(Y0, Y1, y, m, n);

        //Stage 2, multiply element by element given DFT of x and y
        for (int i = 0; i < n; i++){
          Z0[i] = X0[i]*Y0[i] - X1[i]*Y1[i];
          Z1[i] = X1[i]*Y0[i] + X0[i]*Y1[i];
        }

        ifft(z0, z1, Z0, Z1, n);

        stop = max(0, n - 2*m);
        sb.append(Math.round(z0[n - 2]/n));
        for (int i = n - 3; i >= stop; i--){
          sb.append(' ');
          sb.append(Math.round(z0[i]/n));
        }
      }
      sb.append('\n');
    }

    System.out.print(sb.toString());
  }
}
