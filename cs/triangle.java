public class triangle{
  public static int height = 5;
  public static void main(String[] args){
    for(int i = 0; i <= height; i++){
      for(int j = 0; j <= height-i; j++){
        System.out.print(' ');
      }
      for(int k = 0; k < i*2-1; k++){
        System.out.print('x');
      }
      System.out.println();
    }
  }
}
