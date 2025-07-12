import java.util.Scanner;
import java.time.Year;

public class UserInfo {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		
		System.out.print("Enter Your Name:");
		String name = input.nextLine(); //cutting space from front
		
		System.out.print("Enter Your City:");
		String address = input.nextLine();
		
		
		System.out.print("Enter your birth year");
		int birthyear = input.nextInt();
		
		input.nextLine();
		//Calculate age
		int currentYear = Year.now().getValue();
		int age = currentYear - birthyear;
		
		System.out.print("Hello " + name + " from " +address+ " Welcome you are" +age+ "years old");
		
		input.close();

	}

}
