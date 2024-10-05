public class digit{
  public static void main(String[] args){
    System.out.println(mostFrequent(1234566));
  }
  public static int mostFrequent(int num){
    int[] digits = new int[10];
    for(int i = 0; i < 10; i++){digits[i] = 0;}
   
    String str = String.valueOf(num);
    for(int i = 0; i < str.length(); i++){
      digits[(int)(str.charAt(i)-'0')] += 1;
    }
  
    int max = 0;
    int maxIndex = 0;
    for(int i = 0; i < 10; i++){
      if (digits[i] > max){
        max = digits[i];
        maxIndex = i;
      }
    }
   return maxIndex;
  }
}
