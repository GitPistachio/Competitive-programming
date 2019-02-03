import java.util.Scanner;

class ADDREV
{
  public static void main(String[] args)
  {
    Scanner sc = new Scanner(System.in);

    int no_of_cases = sc.nextInt();
    sc.nextLine();
    for (int i=1; i<=no_of_cases; i++)
    {
      StringBuilder pair_of_numbers = new StringBuilder(sc.nextLine());
      String [] numbers = pair_of_numbers.reverse().toString().split(" ");
      int sum_of_reversed_numbers;

      sum_of_reversed_numbers = Integer.valueOf(numbers[0]) + Integer.valueOf(numbers[1]);

      StringBuilder sb = new StringBuilder(Integer.toString(sum_of_reversed_numbers));

      System.out.println(Integer.valueOf(sb.reverse().toString()));
    }
  }
}
