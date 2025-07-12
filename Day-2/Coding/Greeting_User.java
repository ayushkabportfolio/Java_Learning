import java.util.Scanner;
import java.time.LocalTime;
import java.time.Year;

public class Greeting_User {
	
	public static String generateGreeting(String name, int birthyear) {
		int currentYear = Year.now().getValue();
		int age = currentYear - birthyear;
		LocalTime now = LocalTime.now();
	    int hour = now.getHour();
	    String Timegreeting = (hour < 12 ) ? "Good Morning!!" : "Good Afternoon!!";
	    
	    return "Hi " + name + ", " + Timegreeting + " You are " + age + " years old!"; 
	}
	

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Welcome to Greeting!!");
		System.out.println("Enter your name: ");
		String name = input.nextLine();
		//input.nextLine();
		System.out.println("Enter your birthyear: ");
		int birthyear = input.nextInt();
		String finalmessage = generateGreeting(name,birthyear);
		System.out.println(finalmessage);
		input.close();

	}

}
