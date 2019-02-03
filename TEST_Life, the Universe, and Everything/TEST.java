import java.util.Scanner;

class TEST
{
  public static void main(String[] args)
  {
    Scanner sc = new Scanner(System.in);
    int ans;
    do
    {
      ans = sc.nextInt();
      if (ans == 42) break;
      System.out.println(ans);
    } while (true);
  }
}
