import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;


public class calculator implements ActionListener, KeyListener{ 

    JFrame frame;
    JPanel panel;

    //panel elements
    JOptionPane inputPanel;
    static JTextArea screen;
    JScrollPane scrollPane;

    //buttons
    JButton clear;
    JButton equals;
    JButton delete;
    JButton answer;
    JButton sciNotation;

    JButton add;
    JButton multiply;
    JButton subtract;
    JButton divide;

    JButton modulo;
    JButton power;
    JButton root;
    JButton sin;
    JButton cos;
    JButton tan;
    JButton array;
    JButton mean; 
    JButton median;
    JButton range;
    JButton shift;
    JButton factorial;
    JButton incomeTax;
    JButton log;
    JButton log10;
    JButton ln;
    JButton abs;
    JButton least;
    JButton greatest; 
    JButton openParentheses;
    JButton closeParentheses;
    JButton quit;
    JButton left;
    JButton right;
    JButton pi;
    JButton euler;
    JButton combinations;

    JToggleButton degrees;
    static JToggleButton radians;


    JButton dot;
    JButton zero;
    JButton one;
    JButton two;
    JButton three;
    JButton four;
    JButton five;
    JButton six;
    JButton seven;
    JButton eight;
    JButton nine;
 
 
    //global variables
    static double total = 0;
    static ArrayList<String> nums = new ArrayList<String>();

    static String[] FunctionArray = {"log","abs", "ln","log10","sin","cos","tan","asin","acos","atan"};
    static String[] symbolArray = {"+","-","*","/","!","%","^", "√"};
    static String[] numsArray = {"0","1","2","3","4","5","6","7","8","9",".","C","P"};
    static String[] constantsArray = {"π","e"};

    static int cursorIndex = 0; //track cursor position

    static boolean canWriteSymbols = false; //can you write a math symbol

    static boolean numStarted = false; //have you started typing a number

    static boolean canWriteFunc = true; //checks if i just wrote a trig funtion

    static boolean canWriteParenthesis = true; // checks if i can write parenthesis

    static boolean canWriteNegative = true; // check if you cna write a minus sign

    static boolean shifted = false; //check if shift has been pressed

    static boolean emptyLine = true; // check if you are on an empty line

    static int maxParenthesisDepth = 0; //keep track of max perenthesis depth

    static int parenthesisDepth = 0; //track the depth

    static double round = 1000000; //round to constant number
    static double previousAnswer; //save previous answer


    public calculator(){
        //initialize panel and frame
        frame = new JFrame();
        panel = new JPanel();

        //set window size and other stuff
        panel.setBorder(BorderFactory.createEmptyBorder(0,0,700,400));
        panel.setLayout(null);


        //make elements
        inputPanel = new JOptionPane();
        inputPanel.setBounds(400,50,250,250);        
        panel.add(inputPanel);

        screen = new JTextArea(" ");
        screen.setBounds(30,30,340,100);
        screen.setEditable(false);
        screen.addKeyListener(this);
        screen.setAutoscrolls(true);
        panel.add(screen);

        scrollPane = new JScrollPane(screen, JScrollPane.VERTICAL_SCROLLBAR_AS_NEEDED, JScrollPane.HORIZONTAL_SCROLLBAR_AS_NEEDED);
        scrollPane.setBounds(30,30,340,100);
        panel.add(scrollPane);

        //make buttons
        equals = new JButton("=");
        equals.setBounds(322,602,48,48);
        equals.addActionListener(this);
        panel.add(equals);

        clear = new JButton("AC");
        clear.setBounds(322,383,48,48);
        clear.addActionListener(this);
        panel.add(clear);

        shift = new JButton("shift");
        shift.setBounds(30,150,40,20);
        shift.addActionListener(this);
        panel.add(shift);

        left = new JButton("<-");
        left.setBounds(150,150,40,20);
        left.addActionListener(this);
        panel.add(left);

        right = new JButton("->");
        right.setBounds(210,150,40,20);
        right.addActionListener(this);
        panel.add(right);

        quit = new JButton("quit");
        quit.setBounds(270,150,100,20);
        quit.addActionListener(this);
        panel.add(quit);

        mean = new JButton("mean");
        mean.setBounds(90,338,40,20);
        mean.addActionListener(this);
        panel.add(mean);

        median = new JButton("median");
        median.setBounds(150,338,40,20);
        median.setFont(new Font("lucida", Font.PLAIN, 10));
        median.addActionListener(this);
        panel.add(median);

        range = new JButton("range");
        range.setBounds(210,338,40,20);
        range.addActionListener(this);
        panel.add(range);

        least = new JButton("least");
        least.setBounds(270,338,40,20);
        least.addActionListener(this);
        panel.add(least);

        greatest = new JButton("greatest");
        greatest.setBounds(330,338,40,20);
        greatest.setFont(new Font("lucida", Font.PLAIN, 9));
        greatest.addActionListener(this);
        panel.add(greatest);

        incomeTax = new JButton("tax");
        incomeTax.setBounds(330,248,40,20);
        incomeTax.addActionListener(this);
        panel.add(incomeTax);

        add = new JButton("+");
        add.setBounds(249,529,48,48);
        add.addActionListener(this);
        panel.add(add);

        subtract = new JButton("-");
        subtract.setBounds(322,529,48,48);
        subtract.addActionListener(this);
        panel.add(subtract);

        multiply = new JButton("*");
        multiply.setBounds(249,456,48,48);
        multiply.addActionListener(this);
        panel.add(multiply);

        divide = new JButton("/");
        divide.setBounds(322,456,48,48);
        divide.addActionListener(this);
        panel.add(divide);

        modulo = new JButton("%");
        modulo.setBounds(30,248,40,20);
        modulo.addActionListener(this);
        panel.add(modulo);

        factorial = new JButton("!");
        factorial.setBounds(210,248,40,20);
        factorial.addActionListener(this);
        panel.add(factorial);

        combinations = new JButton("nCr");
        combinations.setBounds(270,248,40,20);
        combinations.addActionListener(this);
        panel.add(combinations);

        array = new JButton("array");
        array.setBounds(30,338,40,20);
        array.addActionListener(this);
        panel.add(array);


        power = new JButton("pow");
        power.setBounds(90,248,40,20);
        power.addActionListener(this);
        panel.add(power);

        root = new JButton("root");
        root.setBounds(150,248,40,20);
        root.addActionListener(this);
        panel.add(root);

        sin = new JButton("sin");
        sin.setBounds(210,298,40,20);
        sin.addActionListener(this);
        panel.add(sin);
 
        cos = new JButton("cos");
        cos.setBounds(270,298,40,20);
        cos.addActionListener(this);
        panel.add(cos);

        tan = new JButton("tan");
        tan.setBounds(330,298,40,20);
        tan.addActionListener(this);
        panel.add(tan);

        log10 = new JButton("log10");
        log10.setBounds(90,298,40,20);
        log10.addActionListener(this);
        panel.add(log10);

        log = new JButton("log");
        log.setBounds(30,298,40,20);
        log.addActionListener(this);
        panel.add(log);

        ln = new JButton("ln");
        ln.setBounds(150,298,40,20);
        ln.addActionListener(this);
        panel.add(ln);

        pi = new JButton("π");
        pi.setBounds(30,203,20,20);
        pi.addActionListener(this);
        panel.add(pi);

        euler = new JButton("e");
        euler.setBounds(50,203,20,20);
        euler.addActionListener(this);
        panel.add(euler);

        abs = new JButton("abs");
        abs.setBounds(90,203,40,20);
        abs.addActionListener(this);
        panel.add(abs);

        degrees = new JToggleButton("deg");
        degrees.setBounds(160,203,40,20);
        degrees.addActionListener(this);
        degrees.setSelected(true);
        panel.add(degrees);

        radians = new JToggleButton("rad");
        radians.setBounds(200,203,40,20);
        radians.addActionListener(this);
        radians.setSelected(false);
        panel.add(radians);

        openParentheses = new JButton("(");
        openParentheses.setBounds(270,203,40,20);
        openParentheses.addActionListener(this);
        panel.add(openParentheses);

        closeParentheses = new JButton(")");
        closeParentheses.setBounds(330,203,40,20);
        closeParentheses.addActionListener(this);
        panel.add(closeParentheses);

        zero = new JButton("0");
        zero.setBounds(30,602,48,48);
        zero.addActionListener(this);
        panel.add(zero);

        one = new JButton("1");
        one.setBounds(30,529,48,48);
        one.addActionListener(this);
        panel.add(one);

        two = new JButton("2");
        two.setBounds(103,529,48,48);
        two.addActionListener(this);
        panel.add(two);

        three = new JButton("3");
        three.setBounds(176,529,48,48);
        three.addActionListener(this);
        panel.add(three);

        four = new JButton("4");
        four.setBounds(30,456,48,48);
        four.addActionListener(this);
        panel.add(four);

        five = new JButton("5");
        five.setBounds(103,456,48,48);
        five.addActionListener(this);
        panel.add(five);

        six = new JButton("6");
        six.setBounds(176,456,48,48);
        six.addActionListener(this);
        panel.add(six);

        seven = new JButton("7");
        seven.setBounds(30,383,48,48);
        seven.addActionListener(this);
        panel.add(seven);

        eight = new JButton("8");
        eight.setBounds(103,383,48,48);
        eight.addActionListener(this);
        panel.add(eight);

        nine = new JButton("9");
        nine.setBounds(176,383,48,48);
        nine.addActionListener(this);
        panel.add(nine);

        dot = new JButton(".");
        dot.setBounds(103,602,48,48);
        dot.addActionListener(this);
        panel.add(dot);

        delete = new JButton("del");
        delete.setBounds(249,383,48,48);
        delete.addActionListener(this);
        panel.add(delete);

        answer = new JButton("ans");
        answer.setBounds(249,602,48,48);
        answer.addActionListener(this);
        panel.add(answer);

        sciNotation = new JButton("*10^x");
        sciNotation.setBounds(176,602,48,48);
        sciNotation.addActionListener(this);
        panel.add(sciNotation);

        

        //set frame
        frame.setSize(400,700);
        frame.add(panel, BorderLayout.CENTER);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("Calculator");
        frame.setVisible(true);
    }

    public static void main(String[] args){
        
        new calculator(); 
    }

    //custom methods
    //allow for multiplication with parentheses
    public static void parenthesisMultiplication(){
        for(int i = 0; i < nums.size();i++){
            if(nums.get(i).equals("(") && i!= 0 && isInteger(nums.get(i-1)) && !nums.get(i+1).equals(")")){
                if(i>=2){
                   if(!containsElement(FunctionArray, nums.get(i-2))) {
                    nums.add(i,"*");
                    i++;
                   }
                }
                else{
                nums.add(i,"*");
                i++;
                }
            }
            
            if(nums.get(i).equals(")") && i!= nums.size()-1 && (isInteger(nums.get(i+1)) || nums.get(i+1).equals("("))){
                nums.add(i+1,"*");
                if(nums.get(i+2).equals("(")) i++;
            }
            
        }
    }

    //check if a string is an integer
    public static boolean isInteger(String str){
        //return true or false based on wether parseInt  return an error
        try { 
            int num = Integer.parseInt(str); 
            return true;
        } catch (NumberFormatException e) { 
            return false;
        } 
    }

    //allow for negative numbers
    public static void handleNegatives(){
        for(int i = 0; i < nums.size();i++){
            if(nums.get(i).equals("-")){
                //change the - sign based on wether the next index is a number or not
                if(isInteger(nums.get(i+1))){
                    nums.set(i+1,"-"+nums.get(i+1));
                    nums.remove(i);
                    if(i > 0 && isInteger(nums.get(i-1)))nums.add(i,"+");
                }
                else{
                    nums.set(i,"-1");
                }
                
               
                
            }
        }
    }

    //replace all constants with their values
    public static void replaceConstants(){
        for(int i = 0; i < nums.size();i++){
            if(nums.get(i).equals("π")){
                nums.set(i,String.valueOf(Math.PI));
            }
            if(nums.get(i).equals("e")){
                nums.set(i,String.valueOf(Math.E));
            }
        }
    }

    //check an index and configure the booleans accordingly
    public static void configureBooleans(String previous){
            if(previous.equals("")){
                canWriteFunc = true;
                canWriteParenthesis = true;
                canWriteSymbols = false;
                numStarted = false;
            }
        
            else if(containsElement(symbolArray, previous)){
                canWriteSymbols = true;
                canWriteFunc = true;
                canWriteParenthesis = true;
                numStarted = false;
            }
            else if(containsElement(numsArray, previous) && !previous.equals("P") && !previous.equals("C")){
                canWriteSymbols = true;
                canWriteFunc = false;
                canWriteParenthesis = true;
                numStarted = true;
            }
            else if(containsElement(FunctionArray, previous)){
                canWriteSymbols = false;
                canWriteFunc = true;
                canWriteParenthesis = true;
                numStarted = false;
            }
            else if(containsElement(constantsArray, previous)){
                canWriteSymbols = true;
                canWriteFunc = false;
                canWriteParenthesis = true;
                numStarted = false; 
            }
            else if(previous.equals("C") || previous.equals("P")){
                canWriteParenthesis = true;
                canWriteFunc = true;
                canWriteNegative = true;
                canWriteSymbols = false;
                numStarted = false;
            }

            else if(previous.equals("(")){
                numStarted = false;
                canWriteFunc = true;
                canWriteParenthesis = true;
                canWriteSymbols = false;
                canWriteNegative = true;
            }
           
            else if(previous.equals(")")){
                numStarted = false;
                canWriteFunc = false;
                canWriteParenthesis = true;
                canWriteSymbols = true;
                canWriteNegative = true;
        }
    }

    //turn arraylist into string
    public static String arraylistString(ArrayList<String> list,int beginIndex, int endIndex){
        String foo = "";
        for(int i = beginIndex; i < endIndex;i++){
            foo+=list.get(i);
        }
        return foo;
    }

    //check if array contains an element
    public static boolean containsElement(String[] arr, String element){
        for(String x : arr){
            if (x.equals(element)) return true;
        }
        return false;
    }

    //calculate factorial recursively
    public static Double factorial(Double n){
        n=(double) Math.round(n-0.5);
        if(n<=1) return 1.0;
        return n * factorial(Double.valueOf(n)-1);
    }

    //function to the value before the cursor
    public static void deleteFunc(){
        
        //change th etext on the screen, decrement cursorIndex
        cursorIndex = cursorIndex > 0 ? cursorIndex - 1 : 0;
        //System.out.println(cursorIndex);
        String lastChar = cursorIndex >= 0 ? nums.get(cursorIndex) : "";
        int lineLength = 0;
        for(int i = 0; i < nums.size();i++){
            lineLength += nums.get(i).length();
        }
        String newScreen = screen.getText().substring(0,screen.getText().length()-lineLength);
        for(int i = 0; i < nums.size();i++){
            if (i != cursorIndex) newScreen+=nums.get(i); 
        }
        try{
            //remove index fro araylist
            nums.remove(cursorIndex);
            //nums.add("");
            screen.setText(newScreen);
            numStarted = false;
            if(cursorIndex > 0)configureBooleans(nums.get(cursorIndex-1)); else configureBooleans("");
            //change parentheses depth
            if(lastChar.equals("(")){
                parenthesisDepth--;
            }
            else if(lastChar.equals(")")){
                parenthesisDepth++;
            }   
        }catch(IndexOutOfBoundsException i){}
        lineLength = arraylistString(nums, 0, nums.size()).length();
        screen.setCaretPosition(screen.getText().length()-lineLength + arraylistString(nums, 0, cursorIndex).length());
    }
    
    //write a given symbol to the arraylist and to the screen
    public static void writeSymbols(String symbol){
        try{
            boolean isNum = containsElement(numsArray, symbol);
            boolean isFunc = containsElement(FunctionArray, symbol);
            boolean isParenthesis = symbol.equals("(") || symbol.equals(")");
            boolean isConstant = containsElement(constantsArray, symbol);

            int lineLength = arraylistString(nums, 0, nums.size()).length();
            //String beforeLine = screen.getText().substring(0,screen.getText().length()-lineLength);
            String afterCursor = arraylistString(nums, cursorIndex, nums.size());
            String beforeCursor = screen.getText().substring(0,screen.getText().length()-lineLength)+arraylistString(nums, 0, cursorIndex);
            //System.out.println("before " + beforeCursor + "after " + afterCursor);
            if(isNum || symbol.equals("-")){
                if(symbol.equals("-")){
                    if(canWriteNegative){
                        canWriteSymbols = false;
                        canWriteNegative = false;
                        numStarted = false;
                        canWriteFunc=true;
                        canWriteParenthesis = true;
                        nums.add(cursorIndex,symbol);
                        screen.setText(String.valueOf(beforeCursor + symbol + afterCursor));
                        cursorIndex++;   
                    }
                }
                else if (numStarted) 
                {
                    nums.set(cursorIndex-1,nums.get(nums.size()-1)+symbol);
                    screen.setText(String.valueOf(beforeCursor + symbol + afterCursor));
                    canWriteSymbols = true;
                    numStarted = true;
                    canWriteFunc = false;
                    canWriteNegative = true;
                }
                else if (!symbol.equals(".") && !symbol.equals("C") && !symbol.equals("P")) {
                    nums.add(cursorIndex,symbol);
                    screen.setText(String.valueOf(beforeCursor + symbol + afterCursor));
                    cursorIndex++;
                    canWriteSymbols = true;
                    numStarted = true;
                    canWriteFunc = false;
                    canWriteNegative = true;
                }
                else if(symbol.equals("C") || symbol.equals("P")){
                    nums.add("n"); nums.add(symbol);  nums.add("r");
                    screen.setText(String.valueOf(beforeCursor + "n"+symbol+"r" + afterCursor));
                    cursorIndex+=3;
                    canWriteFunc = false;
                    canWriteParenthesis = true;
                    canWriteSymbols = true;
                    numStarted = false;
                    canWriteNegative = true;
                }
                
                
            }
            else if (canWriteSymbols && !isFunc && !isParenthesis && !isNum && !isConstant){
                canWriteSymbols = false;
                numStarted = false;
                canWriteFunc=true;
                canWriteParenthesis = true;
                canWriteNegative = true;
                nums.add(cursorIndex,symbol);
                screen.setText(String.valueOf(beforeCursor + symbol + afterCursor));
                cursorIndex++;    
            }
            
            else if (isConstant){
                nums.add(cursorIndex,symbol);
                screen.setText(String.valueOf(beforeCursor + symbol + afterCursor));
                cursorIndex++;
                canWriteSymbols = true;
                canWriteFunc = false;
                canWriteNegative = true;
                canWriteParenthesis = true;
                numStarted = false;
            }
            else if (canWriteFunc && isFunc){
                nums.add(cursorIndex,symbol);
                screen.setText(String.valueOf(beforeCursor + symbol + afterCursor));
                beforeCursor += symbol;
                cursorIndex++;
                canWriteSymbols = false;
                numStarted = false;
                canWriteNegative = true;
                canWriteFunc = false;
                canWriteParenthesis = true;

                if(symbol.equals("log")){
                    nums.add(cursorIndex,"x"); 
                    screen.setText(String.valueOf(beforeCursor + "x" + afterCursor));
                    beforeCursor += "x";
                    cursorIndex++;
                }
                
                nums.add(cursorIndex,"("); 
                screen.setText(String.valueOf(beforeCursor + "(" + afterCursor));
                cursorIndex++;
                parenthesisDepth++;
                canWriteFunc=true; 
                canWriteNegative = true;
                canWriteSymbols=false;
                if (parenthesisDepth > maxParenthesisDepth) maxParenthesisDepth = parenthesisDepth;
                
            }
            else if (canWriteParenthesis && isParenthesis){
                if (symbol.equals("(")){ 
                    parenthesisDepth++;
                    canWriteFunc=true; 
                    canWriteSymbols=false;
                    canWriteNegative = true;
                }
                if (symbol.equals(")")){ 
                    parenthesisDepth--; 
                    canWriteFunc=false; 
                    canWriteSymbols=true;
                    canWriteNegative = true;
                }
                if (parenthesisDepth > maxParenthesisDepth) maxParenthesisDepth = parenthesisDepth;
                nums.add(cursorIndex,symbol);
                screen.setText(String.valueOf(beforeCursor + symbol + afterCursor));
                numStarted = false;
                canWriteParenthesis = true;
                cursorIndex++;
                
            }
            emptyLine = false;
            lineLength = arraylistString(nums, 0, nums.size()).length();
            screen.setCaretPosition(screen.getText().length()-lineLength + arraylistString(nums, 0, cursorIndex).length());

            
        }
        catch(NumberFormatException f) {
            System.out.println("Not a number");
        }
            
    }

    //for each symbol, calculate the outcome
    public static void calculateSymbols(int depth, String ...symbol){
        int localDepth = 0;
        String[] last = {"+","-"};
        for(int i = 0; i < nums.size();i++){
            //System.out.println("i am here "+nums + " " + nums.get(i) + " " + localDepth + " " + symbol[0]);
            try{
                //change the localDepth that you are checking
                if(nums.get(i).equals("(")){
                     localDepth++;
                    } 
                if(nums.get(i).equals("(") && localDepth==depth && Arrays.equals(symbol, last)  && (nums.size() == i+2 || nums.get(i+2).equals(")"))){ 
                    nums.remove(i); 
                    try{
                        nums.remove(i+1);
                        localDepth--;
                    }catch(IndexOutOfBoundsException j){}
                    
                }
                if(nums.get(i).equals(")") && (localDepth)==depth && Arrays.equals(symbol, last)){ 
                    nums.remove(i);
                }

                if(nums.get(i).equals(")")){ 
                    localDepth--;
                } 
                //go through each of the operations
                for(String x : symbol){
                    if (nums.get(i).equals(x) && localDepth==depth){
                        boolean isFunc = containsElement(FunctionArray, x);
                        if (x.equals("+")) nums.set(i-1, String.valueOf(Double.valueOf(nums.get(i-1))+Double.valueOf(nums.get(i+1))));     
                        if (x.equals("-")) nums.set(i-1, String.valueOf(Double.valueOf(nums.get(i-1))-Double.valueOf(nums.get(i+1))));
                        if (x.equals("*")) nums.set(i-1, String.valueOf(Double.valueOf(nums.get(i-1))*Double.valueOf(nums.get(i+1))));
                        if (x.equals("/")) nums.set(i-1, String.valueOf(Double.valueOf(nums.get(i-1))/Double.valueOf(nums.get(i+1))));
                        if (x.equals("%")) nums.set(i-1, String.valueOf(Double.valueOf(nums.get(i-1))%Double.valueOf(nums.get(i+1))));
                        if (x.equals("^")) nums.set(i-1, String.valueOf(Math.pow(Double.valueOf(nums.get(i-1)),Double.valueOf(nums.get(i+1)))));
                        if (x.equals("√")) nums.set(i-1, String.valueOf(Math.pow(Double.valueOf(nums.get(i+1)),1/(Double.valueOf(nums.get(i-1))))));
                        if (x.equals("!")) nums.set(i-1, String.valueOf(factorial(Double.valueOf(nums.get(i-1)))));  
                        if (x.equals("log10")) nums.set(i, String.valueOf(Math.log10(Double.valueOf(nums.get(i+1)))));   
                        if (x.equals("ln")) nums.set(i, String.valueOf(Math.log(Double.valueOf(nums.get(i+1)))));
                        if (x.equals("log")) nums.set(i, String.valueOf(Math.log(Double.valueOf(nums.get(i+2)))/Math.log(Double.valueOf(nums.get(i+1)))));
                        if (x.equals("abs")) nums.set(i, String.valueOf(Math.abs(Double.valueOf(nums.get(i+1))))); 
                        if (x.equals("C")) nums.set(i-1, String.valueOf((factorial(Double.valueOf(nums.get(i-1))))/((factorial(Double.valueOf(nums.get(i+1))))*(factorial(Double.valueOf(nums.get(i-1)) - Double.valueOf(nums.get(i+1)))))));
                        if (x.equals("P")) nums.set(i-1, String.valueOf((factorial(Double.valueOf(nums.get(i-1))))/factorial((Double.valueOf(nums.get(i-1)) - Double.valueOf(nums.get(i+1))))));
                        if(radians.isSelected()){
                            if (x.equals("sin")) nums.set(i, String.valueOf(Math.sin(Double.valueOf(nums.get(i+1)))));
                            if (x.equals("cos")) nums.set(i, String.valueOf(Math.cos(Double.valueOf(nums.get(i+1)))));
                            if (x.equals("tan")) nums.set(i, String.valueOf(Math.tan(Double.valueOf(nums.get(i+1)))));
                            if (x.equals("asin")) nums.set(i, String.valueOf(Math.asin(Double.valueOf(nums.get(i+1)))));
                            if (x.equals("acos")) nums.set(i, String.valueOf(Math.acos(Double.valueOf(nums.get(i+1)))));
                            if (x.equals("atan")) nums.set(i, String.valueOf(Math.atan(Double.valueOf(nums.get(i+1)))));
                        }
                        else{
                            if (x.equals("sin")) nums.set(i, String.valueOf(Math.sin(Math.toRadians(Double.valueOf(nums.get(i+1))))));
                            if (x.equals("cos")) nums.set(i, String.valueOf(Math.cos(Math.toRadians(Double.valueOf(nums.get(i+1))))));
                            if (x.equals("tan")) nums.set(i, String.valueOf(Math.tan(Math.toRadians(Double.valueOf(nums.get(i+1))))));
                            if (x.equals("asin")) nums.set(i, String.valueOf(Math.toDegrees(Math.asin(Double.valueOf(nums.get(i+1))))));
                            if (x.equals("acos")) nums.set(i, String.valueOf(Math.toDegrees(Math.acos(Double.valueOf(nums.get(i+1))))));
                            if (x.equals("atan")) nums.set(i, String.valueOf(Math.toDegrees(Math.atan(Double.valueOf(nums.get(i+1))))));
                        }
                        if (!isFunc){
                            nums.remove(i);
                            nums.remove(i);
                        }
                        else{
                            nums.remove(i+1);
                        }
                        i=-1;
                        localDepth = 0;
                    }
                }
            }
        catch(IndexOutOfBoundsException e){}
        }
    }

    //compress all elements in nums to a single element based on order of operations
    public static void solveEquation(){
        if (!screen.getText().equals("")){
            replaceConstants();
            handleNegatives();
            parenthesisMultiplication();
            //check parenthesis depths invidiually
            for(int i = maxParenthesisDepth; i >= 0; i--){
                //order of operations
                //System.out.println(nums);
                calculateSymbols(i,FunctionArray);
                calculateSymbols(i, "C","P");
                calculateSymbols(i,"^","√","!");
                calculateSymbols(i,"*","/","%");
                calculateSymbols(i,"+","-");
                //System.out.println(nums);
            }
            try{
                total = Double.valueOf(nums.get(0));
                total = (Math.round(total*round))/round;
            } catch(IndexOutOfBoundsException o){}
            previousAnswer = total;
            screen.setText(screen.getText() + "\n" +  String.valueOf(total) + "\n\n");
            cursorIndex = 0;
            canWriteSymbols = false;
            canWriteFunc = true;
            numStarted = false;
            canWriteNegative = true;
            emptyLine = true;
            nums.clear();
        }
    }

    @Override
    //when any button is pressed
    public void actionPerformed(ActionEvent e) {
        //check which button was pressed
        calculator.screen.requestFocusInWindow();
        Object s = e.getSource();

       //if any of the following buttons are pressed
       if (java.util.Arrays.asList(zero,one,two,three,four,five,six,seven,eight,nine,dot).contains(s)){
        if(s==zero) writeSymbols("0");
        if(s==one) writeSymbols("1");
        if(s==two) writeSymbols("2");
        if(s==three) writeSymbols("3");
        if(s==four) writeSymbols("4");
        if(s==five) writeSymbols("5");
        if(s==six) writeSymbols("6");
        if(s==seven) writeSymbols("7");
        if(s==eight) writeSymbols("8");
        if(s==nine) writeSymbols("9");
        if(s==dot) writeSymbols(".");

       }
      
       //if a math button is pressed
        if(s!=equals && s!=clear && s!=mean){  

        
                if(s==add){
                    writeSymbols("+");
                }
                if(s==subtract){
                    writeSymbols("-");
                }
                if(s==multiply){
                    writeSymbols("*");
                }
                if(s==divide){
                    writeSymbols("/");
                }
                if(s==modulo){
                    writeSymbols("%");
                }
                if(s==power){
                    writeSymbols("^");
                }
                if(s==root){
                    writeSymbols("√");
                }
                if(s==factorial){
                    writeSymbols("!");
                }
                if(s==log10){
                    writeSymbols("log10");
                }
                if(s==ln){
                    writeSymbols("ln");
                }
                if(s==log){
                    writeSymbols("log");
                }
                if(s==abs){
                    writeSymbols("abs");
                }
                if(s==openParentheses){
                    writeSymbols("(");
                }
                if(s==closeParentheses){
                    writeSymbols(")");
                }
                if(s==pi){
                    writeSymbols("π");
                }
                if(s==euler){
                    writeSymbols("e");
                }
                if(!shifted){
                    if(s==sin){
                        writeSymbols("sin");
                    }
                    if(s==cos){
                        writeSymbols("cos");
                    }
                    if(s==tan){
                        writeSymbols("tan");
                    }
                    if(s==combinations){
                        writeSymbols("C");
                    }
                }
                else{
                    if(s==sin){
                        writeSymbols("asin");
                    }
                    if(s==cos){
                        writeSymbols("acos");
                    }
                    if(s==tan){
                        writeSymbols("atan");
                    }
                    if(s==combinations){
                        writeSymbols("P");
                    }
                }
            }      

        if(s==clear){
        screen.setText("");
        nums.clear();
        cursorIndex = 0;
        canWriteSymbols = false;
        numStarted = false;
        canWriteFunc = true;
        emptyLine = true;
       }
    
       if(s==equals){
        solveEquation();
       }
       
       if(s==degrees){
            if(radians.isSelected()){
                radians.setSelected(false);
            }
            else{
                radians.setSelected(true);
            }
        }

       if(s==radians){
        if(degrees.isSelected()){
            degrees.setSelected(false);
        }
        else{
            degrees.setSelected(true);
        }
       }

       if(s==array){
        try{
        nums.clear();
        int amount = Integer.valueOf(inputPanel.showInputDialog("How many numbers"));
        for(int i = 0; i < amount;i++){
            
                String tmp = inputPanel.showInputDialog("Input number");
                nums.add(tmp);
                screen.setText(screen.getText()+tmp+" ");
            
        }
        screen.setText(screen.getText()+"\n");
        cursorIndex = 0;
        emptyLine = true;
        } catch(NumberFormatException n){}
        }
       if(s==mean || s==median || s==least || s== greatest || s==range){
            
            if (!emptyLine) screen.setText(screen.getText()+"\n");

            double answer = 0;

            ArrayList<Double> numbers = new ArrayList<Double>();
            for(int i = 0; i < nums.size(); i++){
                try{
                    numbers.add(Double.parseDouble(nums.get(i)));
                }catch(NumberFormatException n){}
            }
            Collections.sort(numbers);

            if(s==mean){
                total = 0;
                for(int i = 0; i < numbers.size();i++){
                    total += numbers.get(i);
                }
                double mean = total/numbers.size();
                mean = (Math.round(mean*round))/round;
                answer = mean;
            }
            if(s==median){
                int middle = numbers.size()/2;
                if (numbers.size()%2 == 1) {
                    answer = numbers.get(middle);
                    
                } 
                else{
                    answer = (numbers.get(middle-1) +  numbers.get(middle))/2;
                    
                }

            }
            if(s==range){
                double least = numbers.get(0); double greatest = numbers.get(0);
                for(int i = 0; i < numbers.size();i++){
                    if(numbers.get(i) < least) least = numbers.get(i);
                    if(numbers.get(i) > greatest) greatest = numbers.get(i);
                    answer = greatest-least;
                }
            }
            if(s==least){
                double least = numbers.get(0);
                for(int i = 0; i < numbers.size();i++){
                    if (numbers.get(i) < least) least = numbers.get(i);
                }
                answer = least;
            }
            if(s==greatest){
                double greatest = numbers.get(0);
                for(int i = 0; i < numbers.size();i++){
                    if (numbers.get(i) > greatest) greatest = numbers.get(i);
                }
                answer = greatest;
            }

            screen.setText(screen.getText()+String.valueOf(answer)+"\n\n");
            previousAnswer = answer;
            cursorIndex = 0;
            emptyLine = true;
            canWriteFunc = true;
            canWriteParenthesis = true;
            canWriteSymbols = false;
            numStarted = false;
            nums.clear();
    }
      
        if(s==shift){
        shifted = !shifted;
        if(shifted){
            sin.setText("asin");
            cos.setText("acos");
            tan.setText("atan");
            combinations.setText("nPr");
        }
        else{
            sin.setText("sin");
            cos.setText("cos");
            tan.setText("tan");
            combinations.setText("nCr");
        }
       }
    
       if(s==delete){
        deleteFunc();
       }

       if(s==incomeTax){
        final double TAX_RATE = 0.2;
		final int STANDARD_DEDUCTION = 10000;
		final int ADDITIONAL_DEDUCTION = 2000;

        Double Gross_income = Double.valueOf(inputPanel.showInputDialog("Enter you Gross income"));
        int Dependents = Integer.valueOf(inputPanel.showInputDialog("How many dependents do you have"));

        double Final_gross_income;
		double Final_income_tax;
		
		Final_gross_income = Gross_income;
		Final_gross_income -= STANDARD_DEDUCTION;
		Final_gross_income -= ADDITIONAL_DEDUCTION * Dependents;
		Final_income_tax = Final_gross_income*TAX_RATE;
        screen.setText(screen.getText() + "income Tax: " + Final_income_tax + "\n\n");
       }
    
       if(s==answer){
        nums.add(Double.toString(previousAnswer));
        screen.setText(screen.getText() + Double.toString(previousAnswer));
        cursorIndex++;
        numStarted = true;
        canWriteFunc = false;
        canWriteParenthesis = false;
        canWriteSymbols = true;
       }
    
       if(s==left){
        cursorIndex--;
        if (cursorIndex <= 0) cursorIndex = 0;
        screen.setCaretPosition(screen.getText().length()-arraylistString(nums, 0, nums.size()).length() + arraylistString(nums, 0, cursorIndex).length());
        if(cursorIndex > 0)configureBooleans(nums.get(cursorIndex-1)); else configureBooleans("");
       }
       
       if(s==right){
        cursorIndex++;
        if (cursorIndex > nums.size()) cursorIndex = nums.size();
        screen.setCaretPosition(screen.getText().length()-arraylistString(nums, 0, nums.size()).length() + arraylistString(nums, 0, cursorIndex).length());
        if(cursorIndex > 0)configureBooleans(nums.get(cursorIndex-1)); else configureBooleans("");
       }
       
       if(s==sciNotation){
        nums.add("*");
        nums.add("10");
        nums.add("^");
        screen.setText(screen.getText() + "*10^");
        cursorIndex+=3;
        canWriteFunc = true;
        canWriteParenthesis = true;
        canWriteSymbols = false;
        numStarted = false; 
       }
    
       if(s==quit){
        System.exit(0);
       }
    }

    @Override
    public void keyTyped(KeyEvent e) {
        //System.out.println(e.getKeyCode());
    }

    @Override
    //check if a key was pressed
    public void keyPressed(KeyEvent e) {
        int c = e.getKeyCode();
        String l = Character.toString(e.getKeyChar());
        //System.out.println(c + " " + l);
        if(containsElement(symbolArray, l) || l.equals("(") || l.equals(")")){
            writeSymbols(l);
        }

        else if(l.equals("s")){
            if(!shifted) writeSymbols("sin"); else writeSymbols("asin");
        }
        
        else if(l.equals("c")){
            if(!shifted) writeSymbols("cos"); else writeSymbols("acos");
        }
        
        else if(l.equals("t")){
            if(!shifted) writeSymbols("tan"); else writeSymbols("atan");
        }

        //backspace pressed
        else if(c==8){
            deleteFunc();
        }

        //check if the ascii value corresponds to a number
        else if(c >= 48 && c <= 57 || c==46){
            writeSymbols(l);
            
        }
    
        //enter pressed
        else if(c==10){
            solveEquation();
        }
    
        //left arrow pressed
        else if(c==37){
            cursorIndex--;
            if (cursorIndex <= 0) cursorIndex = 0;
            screen.setCaretPosition(screen.getText().length()-arraylistString(nums, 0, nums.size()).length() + arraylistString(nums, 0, cursorIndex).length()+1);
            if(cursorIndex > 0)configureBooleans(nums.get(cursorIndex-1)); else configureBooleans("");
        }

        //right arrow pressed
        else if(c==39){
            cursorIndex++;
            if (cursorIndex > nums.size()) cursorIndex = nums.size();
            screen.setCaretPosition(screen.getText().length()-arraylistString(nums, 0, nums.size()).length() + arraylistString(nums, 0, cursorIndex).length()-1);
            if(cursorIndex > 0)configureBooleans(nums.get(cursorIndex-1)); else configureBooleans("");
        }
    
        //shift pressed
        else if(c==16){
            shifted = !shifted;
            if(shifted){
                sin.setText("asin");
                cos.setText("acos");
                tan.setText("atan");
                combinations.setText("nPr");
            }
            else{
            sin.setText("sin");
            cos.setText("cos");
            tan.setText("tan");
            combinations.setText("nCr");
        }
        }
    }

    @Override
    public void keyReleased(KeyEvent e) {
        // TODO Auto-generated method stub
    }
}
