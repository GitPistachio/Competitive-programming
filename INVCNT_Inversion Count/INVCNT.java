/*
* Project name : SPOJ: Prime Generator
* Author       : Wojciech Raszka
* Date created : 2019-02-08
* Description  :
* Status       : Accepted (23196092)
* Comment      :
*/

import java.util.Scanner;

class INVCNT{
  public static long merge(int A[], int p, int q, int r){
    int i = p, k = 0, j = q;
    long inv_count = 0;
    int[] T = new int[r - p + 1];

    while (i <= q - 1 && j <= r){
      if (A[i] <= A[j]){
          T[k] = A[i];
          i += 1;
      }
      else{
          T[k] = A[j];
          j += 1;
          inv_count += q - i;
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

    return inv_count;
  }
  public static long mergeSort(int A[], int p, int r){
    long inv_count = 0;
    int q;

    if (p < r){
      q = (p + r)/2;
      inv_count += mergeSort(A, p, q);
      inv_count += mergeSort(A, q + 1, r);
      inv_count += merge(A, p, q + 1, r);
    }
    return inv_count;
  }
  public static void main(String args[]){
      Scanner sc = new Scanner(System.in);
      int T = sc.nextInt();
      int n;


      for (int t=0; t < T; t++){
        n = sc.nextInt();
        int[] A = new int[n];
        for (int i=0; i < n; i++){
          A[i] = sc.nextInt();
        }
        System.out.println(mergeSort(A, 0, n - 1));
      }
  }
}
