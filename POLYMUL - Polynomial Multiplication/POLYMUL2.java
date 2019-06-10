/*
* Project name : SPOJ: POLYMUL - Polynomial Multiplication
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-06-10
* Description  :
* Status       : Accepted (23901442)
* Tags         : java, fast I/O, IFFT, FFT, fast Fourier transform, inveerse fast Fourier transform, polynomial multiplication, bit reverse, logarithm base two, complex numbers, smallest power of two greater than n
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

final class Complex{
  private double re;
  private double im;

  public Complex(double re, double im){
    this.re = re;
    this.im = im;
  }

  public double abs(Complex z){
    return Math.sqrt(this.re*this.re + this.im*this.im);
  }

  public Complex conjugate(){
    return new Complex(this.re, -this.im);
  }

  public Complex add(Complex z){
    return new Complex(this.re + z.re, this.im + z.im);
  }

  public Complex substract(Complex z){
    return new Complex(this.re - z.re, this.im - z.im);
  }

  public Complex multiply(Complex z){
    return new Complex(this.re*z.re - this.im*z.im, this.re*z.im + this.im*z.re);
  }

  public Complex divideByScalar(double x){
    return new Complex(this.re/x, this.im/x);
  }

  public Complex divide(Complex z){
    double alpha = z.re*z.re + z.im*z.im;
    return new Complex((this.re*z.re + this.im*z.im)/alpha, (this.im*z.re - this.re*z.im)/alpha);
  }

  public double re(){
    return this.re;
  }

  public double im(){
    return this.im;
  }

  public Complex copy(){
    return new Complex(this.re, this.im);
  }

  public String toString(){
    if (im <  0) {
      return re + " - " + (-im) + "i";
    }

    return this.re + " + " + this.im + "i";
  }
}

final class FFT{
  public static Complex[] fft2(Complex x[], int m, int n){
    final double mdpi = -6.283185307179586476925286766559;
    int reversed_i, even_idx, odd_idx, L = 1, L2, r, no_of_bits = (int) FuncTools.lg(n);
    Complex[] X = new Complex[n];
    Complex w, e, u, v;

    for (int i = 0; i < n; i++){
      reversed_i = FuncTools.bitReverse(i, no_of_bits);
      if (reversed_i < m){
        X[i] = x[reversed_i].copy();
      } else {
        X[i] = new Complex(0, 0);
      }
    }

    for (int b = 1; b <= no_of_bits; b++){
      L2 = L;
      L <<= 1;
      r = n/L;
      w = new Complex(1, 0);
      e = new Complex(Math.cos(mdpi/L), Math.sin(mdpi/L));

      for (int j = 0; j < L2; j++){
        for (int k = 0; k < r; k++){
          even_idx = k*L + j;
          odd_idx = even_idx + L2;

          u = X[even_idx].copy();
          v = w.multiply(X[odd_idx]);

          X[even_idx] = u.add(v);
          X[odd_idx] = u.substract(v);
        }
        w = w.multiply(e);
      }
    }

    return X;
  }

  public static Complex[] ifft2(Complex X[], int m, int n){
    final double mdpi = 6.283185307179586476925286766559;
    int reversed_i, even_idx, odd_idx, L = 1, L2, r, no_of_bits = (int) FuncTools.lg(n);
    Complex[] x = new Complex[n];
    Complex w, e, u, v;

    for (int i = 0; i < n; i++){
      reversed_i = FuncTools.bitReverse(i, no_of_bits);
      if (reversed_i < m){
        x[i] = X[reversed_i].divideByScalar(n);
      } else {
        x[i] = new Complex(0, 0);
      }
    }

    for (int b = 1; b <= no_of_bits; b++){
      L2 = L;
      L <<= 1;
      r = n/L;
      w = new Complex(1, 0);
      e = new Complex(Math.cos(mdpi/L), Math.sin(mdpi/L));

      for (int j = 0; j < L2; j++){
        for (int k = 0; k < r; k++){
          even_idx = k*L + j;
          odd_idx = even_idx + L2;

          u = x[even_idx].copy();
          v = w.multiply(x[odd_idx]);

          x[even_idx] = u.add(v);
          x[odd_idx] = u.substract(v);
        }
        w = w.multiply(e);
      }
    }

    return x;
  }
}

final class FuncTools{
  public static int getSmallestPowerOf2(int n){
    // Return the smallest power of 2 greater than given number

    int i = 1;

    while (i < n){
      i <<= 1;
    }

    return i;
  }

  public static int bitReverse(int n, int no_of_bits){
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

  public static double lg(double x){
    return Math.log(x)/Math.log(2);
  }
}

final class POLYMUL2{
  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    int T = r.nextPositiveInt();
    int m, n, degree_of_polynominal, stop;
    Complex[] x, y, z, X, Y, Z;

    while (T-- > 0){
      degree_of_polynominal = r.nextPositiveInt();
      m = FuncTools.getSmallestPowerOf2(degree_of_polynominal + 1);
      n = m << 1;

      x = new Complex[degree_of_polynominal + 1];
      y = new Complex[degree_of_polynominal + 1];

      for (int i = 0; i <= degree_of_polynominal; i++){
        x[i] = new Complex(r.nextPositiveInt(),0);
      }

      for (int i = 0; i <= degree_of_polynominal; i++){
        y[i] = new Complex(r.nextPositiveInt(),0);
      }

      X = FFT.fft2(x, degree_of_polynominal + 1, n);
      Y = FFT.fft2(y, degree_of_polynominal + 1, n);

      Z = new Complex[n];
      for (int i = 0; i < n; i++){
        Z[i] = X[i].multiply(Y[i]);
      }

      z = FFT.ifft2(Z, n, n);

      stop = degree_of_polynominal << 1;
      sb.append(Math.round(z[0].re()));
      for (int i = 1; i <= stop; i++){
        sb.append(' ');
        sb.append(Math.round(z[i].re()));
      }
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
