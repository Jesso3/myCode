import java.util.*;

public class dice{
  public static void main(String[] args){
      Random rand = new Random();

    int n1 = 0;
    int n2 = 0;
    int counter = 0;
    while (n1 + n2 != 7){
      n1 = rand.nextInt(6)+1;
      n2 = rand.nextInt(6)+1;
      System.out.println(n1 + " + " + n2 + " = " + (n1+n2));
      counter++;
    }
    System.out.println("You won after " + counter + " tries!");
  
  }

}
