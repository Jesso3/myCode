public class cheat {
    public static void whileMystery(int x, int y) {
    int s = 0;

    while (x > 0 && 2 * y >= x) {
        System.out.print(s + " ");
        y = y - x;
        x--;
        s = s + x;
    }

    System.out.println(s);
}

    public static void main(String[] args) {
       whileMystery(-2, -6);	
whileMystery(2, 3);	
whileMystery(4, 8);	
whileMystery(5, 40);	
whileMystery(10, 31);


    }
}
