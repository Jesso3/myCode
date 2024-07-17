package Graphics;

import java.util.Scanner;
import java.util.ArrayList;

public class AccessingDigits {

	public static void main(String[] args) {
		
		ArrayList<Integer> numbers = new ArrayList<Integer>();
		
		Scanner reader = new Scanner (System.in);
		
		System.out.print("Enter an Integer: ");
		int numInt = reader.nextInt();
		
		System.out.print("Enter a double: ");
		double numDouble = reader.nextDouble();
		
		int num = numInt;
		
		while (num > 0) {
	         int digit = num % 10;
	         numbers.add(numbers.size(),digit);
	         num = num / 10;
		}
		
		int sum = 0;
		for (int i = 0; i < numbers.size();i++) {
			
			sum += numbers.get(i);
		}
		
		System.out.println(numbers.get(0));
		System.out.println(numbers.get(1));
		System.out.println(sum);
		System.out.println(numDouble - (int)numDouble);
		System.out.println((int)((numDouble - (int)numDouble)*10));
		
		
		reader.close();
		
	}

}



