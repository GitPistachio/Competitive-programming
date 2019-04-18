/*
* Project name : SPOJ: FINDPRM - Finding Primes
* Author       : Wojciech Raszka
* E-mail       : gitpistachio@gmail.com
* Date created : 2019-03-16
* Description  :
* Status       : Accepted (23427021)
* Tags         : c++, fast I/O,  floor binary search, dynamic programming, sieve of eratosthenes
* Comment      : Used knowledge from ALICESIE and standard precomputation of sieve of eratosthenes
*/

#include <stdio.h>

inline void readUnsignedIInt(int *n)
{
    register char c = 0;
    while (c < 33) c=getc_unlocked(stdin);
    (*n) = 0;
    while (c>32) {(*n)=(*n)*10LL + (c-48); c=getc_unlocked(stdin);}
}

inline int floorBinarySearch(int arr[], int l, int r, int key){
  if (arr[l] > key)
    return -1;

  int m;
  while (r - l > 1){
    m = l + (r - l)/2;

    if (arr[m] <= key)
      l = m;
    else
      r = m;
  }
  return l;
}

int main(){
  const int MAX_N = 10000000;
  const int NO_OF_PRIMES_BETWEEN_2_AND_MAX_N = 664579;
  bool is_not_prime[MAX_N + 1] = {false};
  int no_of_primes = 0;
  int primes[NO_OF_PRIMES_BETWEEN_2_AND_MAX_N];

  for (int i = 4; i <= MAX_N; i += 2){
    is_not_prime[i] = true;
  }
  for (int p = 3; p*p <= MAX_N; p += 2){
    if (is_not_prime[p] == false){
      for (int i = p*p; i <= MAX_N; i += p){
        is_not_prime[i] = true;
      }
    }
  }
  primes[no_of_primes++] = 2;
  for (int p = 3; p <= MAX_N; p += 2){
    if (is_not_prime[p] == false){
      primes[no_of_primes++] = p;
    }
  }

  int T;
  int n;

  readUnsignedIInt(&T);

  while (T-- > 0){
    readUnsignedIInt(&n);

    printf("%d\n", floorBinarySearch(primes, 0, NO_OF_PRIMES_BETWEEN_2_AND_MAX_N, n) - floorBinarySearch(primes, 0, NO_OF_PRIMES_BETWEEN_2_AND_MAX_N, n/2));
  }
  return 0;
}
