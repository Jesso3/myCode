import java.util.*;
public class scores{
  public static void main(String[] args){
   askScores();
  }
  public static void askScores(){
    Scanner console = new Scanner(System.in);
    int[] scores = new int[100];
    for(int i = 0; i < 100; i++){scores[i] = 0;}
    System.out.print("how many scores: ");
    int num = console.nextInt();
    for(int i = 0; i < num; i++){
      System.out.print("Score " + (i+1) + ": ");
      scores[console.nextInt()] += 1;
    }
    for(int i = 0; i < 100; i++){
      if(scores[i] > 0){
      System.out.print(i + ": ");
      for(int j = 0; j < scores[i]; j++){
        System.out.print("*");
      }
      System.out.println();
      }
    }
    
  }
}
