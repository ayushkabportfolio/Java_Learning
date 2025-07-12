import java.util.Scanner;
public class Check_Even_or_Odd {
	public static void evenorodd(int a) {
		/* if else
		if (a%2 == 0)
		{
			System.out.println("Even Number");
		}
		else 
			System.out.println("Odd Number");*/
		
		System.out.println((a % 2 == 0) ? "Even Number" : "Odd Number");//one life if else
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);
		System.out.println("Welcome to code to get Even or Odd number detection");
		System.out.println("Give input to check the number: ");
		int a = input.nextInt();
		
		evenorodd(a);
		
		input.close();

	}

}
