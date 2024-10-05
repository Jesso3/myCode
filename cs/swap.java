      import java.util.*;

public class swap{
  public static void main(String[] args){

    int[] a1 = {12,34,56};
    swap1(a1,1,2);
    System.out.println(Arrays.toString(a1));

    int a = 7;
    int b = 35;
    swap2(a,b);
  }
  public static void swap1(int[] arr, int index1, int index2){
    int tmp = arr[index1];
    arr[index1] = arr[index2];
    arr[index2] = tmp;
  }
  public static void swap2(int a, int b){
    int tmp = a;
    a = b;
    b = tmp;
    System.out.println(a + " " + b);
  }
}
