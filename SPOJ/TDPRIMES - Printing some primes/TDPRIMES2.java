/*
* Project name : SPOJ: TDPRIMES - Printing some primes
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2019-04-21
* Description  :
* Status       : Accepted (23666596)
* Tags         : java, fast I/O, prime numbers, sieve of eratosthenes, 2-3 wheel factorization
* Comment      :
*/

import java.lang.StringBuilder;

final class TDPRIMES2{
  public static void main(String args[]){
    StringBuilder sb = new StringBuilder();

    final int MAX_N = 100000000;
    boolean[] is_not_prime = new boolean[MAX_N + 1];
    int p, no_of_primes = 0;
    int[] wheel = {2,4};
    boolean run;

    run = true;
    p = 5;
    for (int i = p*p; i <= MAX_N; i += p){
		is_not_prime[i] = true;
	}
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

    sb.append("2\n");
    no_of_primes += 3;

    run = true;
    p = 5;
    while (run){
      for (int w:wheel){
        p += w;
        if (p > MAX_N) {
          run = false;
          break;
        }
        if (is_not_prime[p] == false){
          if (no_of_primes++ % 100 == 0){
            sb.append(p);
            sb.append('\n');
          }
        }
      }
    }

    System.out.print(sb.toString());
  }
}
