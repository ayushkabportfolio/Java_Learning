import java.util.Scanner;

public class swaptwonumbers {
	public static void swapnumbers(int a, int b) {
		System.out.println("Before Swapping: A= " +a+ " B= " +b);
		a= a+b;
		b= a-b;
		a= a-b;
		System.out.println("After Swapping: A= " +a+ " B= " +b);
	}
	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Welcome to swapping of number game");
		System.out.println("Enter number 1: ");
		int a = input.nextInt();
		System.out.println("Enter number 2: ");
		int b = input.nextInt();
		swapnumbers(a,b);
		input.close();
		
	}

}
