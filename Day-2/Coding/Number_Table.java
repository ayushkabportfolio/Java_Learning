import java.util.Scanner;

public class Number_Table {
	public static void table(int a, int b) {
		
		for (int i = 1 ; i<= b ; i++) {
			System.out.println(a +" x " + i + " = " +(a*i));
		}
	}

	public static void main(String[] args) {
	    Scanner input = new Scanner(System.in);
	    System.out.println("Enter the Number for generating table: ");
	    int a = input.nextInt();
	    System.out.println("Enter the Range for generating table: ");
	    int b = input.nextInt();
	    table(a,b);
	    input.close();
		

	}

}
