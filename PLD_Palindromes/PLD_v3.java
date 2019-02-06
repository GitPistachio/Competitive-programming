//TLE
import java.util.Scanner;

class PLD_v3{
  static int P = 101;
  static int MOD = 1000000007;

  public static long modPower(long base, long exponent){
    if (exponent == 0)
      return 1;
    if (exponent == 1)
      return base;

    long temp = modPower(base, exponent/2);

    if (exponent % 2 == 0)
      return (temp*temp) % MOD;
    else
      return (((temp*temp) % MOD) * base) % MOD;
  }

  public static long modMultiplicativeInverse(long n){
    return modPower(n, MOD - 2);
  }

  public static void computePower(long[] power, int n){
    power[0] = 1; //101^0 = 1
    for (int i=1; i <= n; i++)
      power[i] = (power[i - 1] * P)  % MOD; // P % MOD = P
  }

  public static void computePrefixHash(char[] str, int n, long[] prefix_hash, long[] power){
    prefix_hash[0] = 0;
    prefix_hash[1] = str[0];

    for (int i=2; i<=n; i++)
      prefix_hash[i] = (prefix_hash[i - 1] + (str[i - 1] * power[i - 1] ) % MOD) % MOD;
  }

  public static void computeSuffixHash(char[] str, int n, long[] suffix_hash, long[] power){
    suffix_hash[0] = 0;
    suffix_hash[1] = str[n - 1];

    for (int i=n - 2, j=2; i >=0 && j <= n; i--, j++)
      suffix_hash[j] = (suffix_hash[j - 1] + (str[i] * power[j - 1]) % MOD) % MOD;
  }

  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int K = sc.nextInt(); sc.nextLine();

    char[] str = sc.nextLine().toCharArray();

    int n = str.length;

    long[] power = new long[n + 1];
    computePower(power, n);

    long[] prefix_hash = new long[n + 1];
    long[] suffix_hash = new long[n + 1];

    computePrefixHash(str, n, prefix_hash, power);
    computeSuffixHash(str, n, suffix_hash, power);

    long[] modMI = new long[n + 1];

    for (int i=0; i <= n - K; i++)
      modMI[i] = modMultiplicativeInverse(power[i]);

    int no_of_pld = 0;
    long word_hash, reversed_word_hash;
    boolean is_pld;
    for (int i=0; i <= n - K; i++){
        word_hash = ((prefix_hash[i + K] - prefix_hash[i] + MOD) % MOD * modMI[i]) % MOD;
        reversed_word_hash = ((suffix_hash[n - i] - suffix_hash[n - i - K] + MOD) % MOD * modMI[n - i - K]) % MOD;
        if (word_hash == reversed_word_hash){
          is_pld = true;
          for (int k=0; k <= K/2; k++){
            if (str[i + k] != str[i + K - k - 1]){
              is_pld = false;
              break;
            }
          }
          if (is_pld)
            no_of_pld++;
        }
    }
    System.out.println(no_of_pld);
  }
}
