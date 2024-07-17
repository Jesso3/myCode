package Graphics;

import java.util.Arrays;
import java.util.Scanner;

public class Weather {

	public static void main(String[] args) {
		
		Scanner reader = new Scanner (System.in);
		
 		double Average = 0;
		int aboveAverage = 0;
		           
		System.out.print("How many days Tempratures: ");
		int days = reader.nextInt();
		
		int[] temps = new int[days];
		
		for (int i = 0; i < days;i++) {
            System.out.print(String.format("Day %d's high temp is: ", i+1));
            temps[i] = reader.nextInt();
            Average+=temps[i];  
		}
		
		Average/=temps.length;
		
		for (int x : temps) {
			if (x > Average) {
				aboveAverage++;
			}
		}
		
		Arrays.sort(temps);
		
		System.out.println(String.format("Average Temp is = %f", Average));
		System.out.println(String.format("%d days were above average", aboveAverage));
		System.out.println(String.format("Two coldest days: %d, %d", temps[0], temps[1]));
		System.out.println(String.format("Two hottest days: %d, %d", temps[temps.length-1], temps[temps.length-2]));

		reader.close();

	}
}
