/*
* Project name : SPOJ: TDPRIMES - Printing some primes
* Author       : Wojciech Raszka
* E-mail       : contact@gitpistachio.com
* Date created : 2019-04-21
* Description  :
* Status       : Accepted (23666715)
* Tags         : java, fast I/O, prime numbers, sieve of eratosthenes, 2-3-5 wheel factorization, wheel sieve
* Comment      :
*/

import java.lang.StringBuilder;

final class TDPRIMES3{
  public static void main(String args[]){
    StringBuilder sb = new StringBuilder();

    final int MAX_N = 100000000;
    boolean[] is_not_prime = new boolean[MAX_N + 1];
    int p, no_of_primes = 0;
    int[] wheel = {6,4,2,4,2,4,6,2};
    int[] primes = {7,11,13,17,19,23,29,31};
    boolean run;

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

    sb.append("2\n");
    no_of_primes += 11;

    run = true;
    p = 31;
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
