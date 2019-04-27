/*
* Project name : SPOJ: TSORT - Turbo Sort
* Author       : Wojciech Raszka
* E-mail       : gitpistachio.gmail.com
* Date created : 2019-04-24
* Description  :
* Status       : Accepted (23681127, 23682129, 23685592, 23690652)
* Tags         : java, fast I/O, sorting, bubble sort, optimized bubble sort, insertion sort, selection sort, heap sort, merge sort, median of three quick sort, hybrid introspective quick sort, optimized hybrid introspective quick sort
* Comment      : builtin sorting function 0.3s, bubble sort TLE, optimized bubble sort TLE, insertion sort TLE, selection sort TLE, heap sort 0.3, merge sort 0.33, median of three quick sort TLE, hybrid introspective quick sort 0.56s, optimized hybrid introspective quick sort 0.31s
*/

import java.lang.StringBuilder;
import java.io.DataInputStream;
import java.io.IOException;
import java.util.Arrays;
import java.lang.Math;

final class TSORT{
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

  public static void bubbleSort(int A[]){
    int n = A.length;
    int a;

    for (int i = 0; i < n - 1; i++){
      for (int j = 0; j < n - i - 1; j++){
        if (A[j] > A[j + 1]){
          a = A[j];
          A[j] = A[j + 1];
          A[j + 1] = a;
        }
      }
    }
  }

  public static void optimizedBubbleSort(int A[]){
    int n = A.length;
    int a;
    boolean is_swapped;

    for (int i = 0; i < n - 1; i++){
      is_swapped = false;
      for (int j = 0; j < n - i - 1; j++){
        if (A[j] > A[j + 1]){
          a = A[j];
          A[j] = A[j + 1];
          A[j + 1] = a;
          is_swapped = true;
        }
      }
      if (is_swapped == false) break;
    }
  }

  public static void insertionSort(int A[]){
    int n = A.length;
    int key;
    int j;

    for (int i = 1; i < n; i++){
        key = A[i];
        j = i - 1;
        while (j >= 0 && A[j] > key){
          A[j + 1] = A[j];
          j--;
        }
        A[j + 1] = key;
    }
  }

  public static void selectionSort(int A[]){
    int n = A.length;
    int min_idx;
    int a;

    for (int i = 0; i < n - 1; i++){
      min_idx = i;
      for (int j = i + 1; j < n; j++){
        if (A[j] < A[min_idx]){
          min_idx = j;
        }

        a = A[min_idx];
        A[min_idx] = A[i];
        A[i] = a;
      }
    }
  }

  public static void heapify(int A[], int n, int i){
    int largest = i;
    int l = 2*i + 1;
    int r = 2*i + 2;
    int a;

    if (l < n && A[l] > A[largest]){
      largest = l;
    }

    if (r < n && A[r] > A[largest]){
      largest = r;
    }

    if (largest != i){
      a = A[i];
      A[i] = A[largest];
      A[largest] = a;

      heapify(A, n, largest);
    }
  }

  public static void heapSort(int A[]){
    int n = A.length;
    int a;

    for (int i = n/2 - 1; i >= 0; i--){
      heapify(A, n, i);
    }

    for (int i = n - 1; i >= 0; i--){
      a = A[0];
      A[0] = A[i];
      A[i] = a;

      heapify(A, i, 0);
    }
  }

  public static void merge(int A[], int p, int q, int r){
    int i = p, k = 0, j = q;
    int[] T = new int[r - p + 1];

    while (i <= q - 1 && j <= r){
      if (A[i] <= A[j]){
          T[k] = A[i];
          i += 1;
      }
      else{
          T[k] = A[j];
          j += 1;
      }
      k += 1;
    }

    if (i <= q - 1){
      while (i <= q - 1){
        T[k] = A[i];
        i += 1;
        k += 1;
      }
    }
    else{
      while (j <= r){
        T[k] = A[j];
        j += 1;
        k += 1;
      }
    }

    for (i = 0; i < r - p + 1; i++){
      A[p + i] = T[i];
    }
  }
  public static void mergeSort(int A[], int p, int r){
    int q;

    if (p < r){
      q = (p + r)/2;
      mergeSort(A, p, q);
      mergeSort(A, q + 1, r);
      merge(A, p, q + 1, r);
    }
  }

  public static int medianOfThreePivot(int A[], int l, int r){
    int m = l + (r - l)/2;
    int a;

    if (A[r] < A[l]){
      a = A[l];
      A[l] = A[r];
      A[r] = a;
    }

    if (A[m] < A[l]){
      a = A[l];
      A[l] = A[m];
      A[m] = a;
    }

    if (A[r] < A[m]){
      a = A[m];
      A[m] = A[r];
      A[r] = a;
    }

    return m;
  }

  public static int partition(int A[], int l, int r){
    int a;
    int pivot_idx = medianOfThreePivot(A, l, r);
    int pivot = A[pivot_idx];
    int i = l;

    A[pivot_idx] = A[r];
    A[r] = pivot;

    while (l < r){
      if (A[l] <= pivot){
        a = A[i];
        A[i] = A[l];
        A[l] = a;
        i++;
      }
      l++;
    }

    a = A[i];
    A[i] = A[r];
    A[r] = a;

    return i;
  }

  public static void quickSort(int A[], int l, int r){
    if (l < r){
      int i = partition(A, l, r);
      quickSort(A, l, i - 1);
      quickSort(A, i + 1, r);
    }
  }

  public static void introSort(int A[], int l, int r, int max_depth){
    if (max_depth == 0){
      heapSort(A);
    } else if (r - l > 8) {
        int i = partition(A, l, r);
        introSort(A, l, i - 1, max_depth - 1);
        introSort(A, i + 1, r, max_depth - 1);
    }
  }

  public static void hybridIntrospectiveSort(int A[]){
    int n = A.length;
    int max_depth = (int)Math.floor(Math.log(n))*2;

    introSort(A, 0, n - 1, max_depth);
    insertionSort(A);
  }

  public static boolean optimizedIntroSort(int A[], int l, int r, int max_depth){
    if (max_depth == 0){
      heapSort(A);
      return false;
    } else if (r - l > 8) {
        int i = partition(A, l, r);
        if (introSort(A, l, i - 1, max_depth - 1)){
            if (introSort(A, i + 1, r, max_depth - 1)){
              return true;
            } else {
              return false;
            }
        } else {
          return false;
        }
    }
    return true;
  }

  public static void optimizedHybridIntrospectiveSort(int A[]){
    int n = A.length;
    int max_depth = (int)Math.floor(Math.log(n))*2;

    if (introSort(A, 0, n - 1, max_depth)){
        insertionSort(A);
    }

  }

  public static void main(String args[]) throws IOException{
    Reader r = new Reader();
    StringBuilder sb = new StringBuilder();
    int n = r.nextUnsignedInt();
    int[] A = new int[n];

    for(int i =  0; i < n; i++){
      A[i] = r.nextUnsignedInt();
    }

    //Arrays.sort(A); //0.3s
    //bubbleSort(A); //TLE
    //optimizedBubbleSort(A); //TLE
    //insertionSort(A); //TLE
    //selectionSort(A); //TLE
    //heapSort(A); //0.3s
    //mergeSort(A, 0, n - 1); //0.33s
    //quickSort(A, 0, n - 1); //TLE
    //hybridIntrospectiveSort(A); //0.56s
    optimizedHybridIntrospectiveSort(A); //0.31s

    for(int i =  0; i < n; i++){
      sb.append(A[i]);
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
