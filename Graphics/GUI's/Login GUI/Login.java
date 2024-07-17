import javax.imageio.ImageIO;
import javax.swing.*;
import javax.swing.event.ChangeEvent;
import javax.swing.event.ChangeListener;

import java.awt.*;
import java.awt.event.*;
import java.awt.image.BufferedImage;
import java.io.*;
import java.util.Scanner;
import java.util.HashMap;


public class Login implements ActionListener, MouseListener, ChangeListener {

    private JFrame frame;

    //variables for login page
    private JPanel Login;
    private static JTextField userText;
    private static JPasswordField passwordText;
    private static JLabel success;
    private JButton log;
    private JButton create;
    private JSlider redSlider;
    private JSlider blueSlider;
    private JSlider greenSlider;

    //variables for main page
    private JPanel Main;
    private JButton Logout;
    private JButton fontLeft;
    private JButton fontRight;


    //global variables
    static int w = 500;
    static int h = 300;
    static String[] fonts = {"Lucida", "Times New Roman","Arial"};
    static int fontIndex = 1;

    static String detailsPath = "/Users/jesse/Desktop/python_code/Graphics/GUI's/Login GUI/details.txt";

    private static HashMap<String, String> people = new HashMap<String, String>();

    public Login() {
        frame = new JFrame();
        Login= new JPanel();
        Main = new JPanel();

        frame.setSize(w, h);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("Login GUI");

        Login.setLayout(null);
        Main.setLayout(null);

        Login.addMouseListener(this);
        Login.setBackground(new Color(255,255,255));

        // Add elements to Login screen
        JLabel userLabel = new JLabel("User:");
        userLabel.setBounds(w/35, h/10, (int)(w/4.375), h/8);
        userLabel.setFont(new Font(fonts[fontIndex], Font.PLAIN, (int)((w/4.375) + h/8)/10));
        Login.add(userLabel);

        userText = new JTextField(20);
        userText.setBounds((int)(w/3.5), h/10, (int)(w/2.12), h/8);
        userText.setFont(new Font(fonts[fontIndex], Font.PLAIN, (int)((w/2.12) + h/8)/18));
        userText.setText("");
        Login.add(userText);

        JLabel passwordLabel = new JLabel("Password:");
        passwordLabel.setBounds(w/35, h/4, (int)(w/4.375), h/8);
        passwordLabel.setFont(new Font(fonts[fontIndex], Font.PLAIN, (int)((w/4.375) + h/8)/10));
        Login.add(passwordLabel);

        passwordText = new JPasswordField();
        passwordText.setBounds((int)(w/3.5), h/4, (int)(w/2.12), h/8);
        userText.setFont(new Font(fonts[fontIndex], Font.PLAIN, (int)((w/2.12) + h/8)/18));
        passwordText.setText("");
        Login.add(passwordText);

        
        log = new JButton("Login");
        log.setBounds(w/35, (int)(h/2.5), (int)(w/4.375), h/8);
        log.setFont(new Font(fonts[fontIndex], Font.PLAIN, (int)((w/4.375) + h/8)/10));
        log.addActionListener(this);
        Login.add(log);

        create = new JButton("Create Login");
        create.setBounds((int)(w/3.5), (int)(h/2.5), (int)(w/2), h/8);
        create.setFont(new Font(fonts[fontIndex], Font.PLAIN, (int)((w/2) + h/8)/19));
        create.addActionListener(this);
        Login.add(create);

        success = new JLabel("");
        success.setBounds(w/35, (int)(h/1.81), (int)(w/1.17), h/8);
        success.setFont(new Font(fonts[fontIndex], Font.PLAIN, (int)((w/1.17) + h/8)/31));
        Login.add(success);

        redSlider = new JSlider(0,255,0);
        redSlider.setBounds(10,160,400,25);
        redSlider.addChangeListener(this);
        Login.add(redSlider);

        greenSlider = new JSlider(0,255,0);
        greenSlider.setBounds(10,185,400,25);
        greenSlider.addChangeListener(this);
        Login.add(greenSlider);

        blueSlider = new JSlider(0,255,0);
        blueSlider.setBounds(10,210,400,25);
        blueSlider.addChangeListener(this);
        Login.add(blueSlider);



        //add elements to Main screen
        Logout = new JButton("Log out");
        Logout.setBounds((int)(w/1.4),(int)(h/1.6),(int)(w/4.67),h/8);
        Logout.setFont(new Font(fonts[fontIndex], Font.PLAIN, (int)((w/4.67) + h/8)/10));
        Logout.addActionListener(this);
        Main.add(Logout);

        fontLeft = new JButton("previous font");
        fontLeft.setBounds((int)(w/10),(int)(h/10),(int)(w/3),h/8);
        fontLeft.setFont(new Font(fonts[fontIndex], Font.PLAIN, (int)((w/2.5) + h/8)/14));
        fontLeft.addActionListener(this);
        Main.add(fontLeft);

        fontRight = new JButton("next font");
        fontRight.setBounds((int)(w/2),(int)(h/10),(int)(w/3),h/8);
        fontRight.setFont(new Font(fonts[fontIndex], Font.PLAIN, (int)((w/2.5) + h/8)/14));
        fontRight.addActionListener(this);
        Main.add(fontRight);

        BufferedImage bugImage;
        try {
            bugImage = ImageIO.read(new File("/Users/jesse/Desktop/python_code/Graphics/GUI's/Login GUI/images/bug.jpg"));
            int width = 150;
            int height = (int)(width*1.265625);
            bugImage = resize(bugImage,frame.getWidth(),frame.getHeight());
            JLabel bugLabel = new JLabel(new ImageIcon(bugImage));
            bugLabel.setBounds(0,0,frame.getWidth(),frame.getHeight());
            Main.add(bugLabel);
        } catch (IOException e) {
            System.out.println("didn't work");
            e.printStackTrace();
        }
       

        frame.add(Login);
        Login.setVisible(true);
        frame.setVisible(true);
    }

    //custom methods
    public static void loadPeople(){
        try {
            File myObj = new File(detailsPath);
            Scanner myReader = new Scanner(myObj);
            while (myReader.hasNextLine()) {
                String line = myReader.nextLine();
                String[] parts = line.split(", ");
                try{
                    people.put(parts[0],parts[1]);
                } catch (ArrayIndexOutOfBoundsException o) {
                    continue;
                }  
            }
            //System.out.println(data);
            myReader.close();
            } catch (FileNotFoundException o) {
            System.out.println("An error occurred.");
            o.printStackTrace();
            }
    }

    public static BufferedImage resize(BufferedImage img, int newW, int newH) {  
        int w = img.getWidth();  
        int h = img.getHeight();  
        BufferedImage dimg = new BufferedImage(newW, newH, img.getType());  
        Graphics2D g = dimg.createGraphics();  
        g.setRenderingHint(RenderingHints.KEY_INTERPOLATION,
        RenderingHints.VALUE_INTERPOLATION_BILINEAR);  
        g.drawImage(img, 0, 0, newW, newH, 0, 0, w, h, null);  
        g.dispose();  
        return dimg;  
    }  

    public static void reset(){
        userText.setText("");
        passwordText.setText("");
        success.setText("");
    }

    public static void setFonts(JPanel panel){
        for( int i = 0; i < panel.getComponentCount(); i++ ) {
            int compWidth = panel.getComponent(i).getWidth();
            int compHeight = panel.getComponent(i).getHeight();
            int division = (int)((compWidth + compHeight)/(15 * (w/500)));
            panel.getComponent(i).setFont(new Font(fonts[fontIndex], Font.PLAIN, (int)(compWidth+compHeight)/division));
        }
    }
    public static void main(String[] args) {
        loadPeople();
        new Login();
    }

    //if a button is pressed
    @Override
    public void actionPerformed(ActionEvent e) {
        if(e.getSource()==log){  
    

            String user = userText.getText();
            String password = passwordText.getText();

            for (String i : people.keySet()) {
                if (user.equals(i) && people.get(i).equals(password)){
                    success.setText("Logged in");
                    Login.setVisible(false);;
                    frame.remove(Login);  
                    frame.add(Main);
                    Main.setVisible(true);
                    break;
                }
                else{
                    success.setText("Invalid Login");
                }
            }
        }
    
        if (e.getSource()==create){
            String user = userText.getText();
            String password = passwordText.getText();

            //validate password
            Boolean valid = true;
            Boolean[] checks = {false,false,false,true}; // length, caps, nums, no non alphabetic characters
            String[] errorStrings = {"password must be greater than 5 characters", "password must include a capital letter", "password must include a number", "password can't include non alphabetic characters"};

            if (password.length() >= 5) checks[0] = true;

            for(int i = 0; i < password.length(); i++){
                if (Character.isUpperCase(password.charAt(i))) checks[1] = true;
                if (Character.isDigit(password.charAt(i))) checks[2] = true;

                if (!Character.isLetter(password.charAt(i)) && !Character.isDigit(password.charAt(i))) checks[3] = false;
            }

            for(int i = 0; i < checks.length;i++){
                if (!checks[i]){
                    valid = false;
                    success.setText(errorStrings[i]);
                    break;
                }
            }

            //if password is valid
            if(valid){
                //read file
                String data = "";

                try {
                File myObj = new File(detailsPath);
                Scanner myReader = new Scanner(myObj);
                while (myReader.hasNextLine()) {
                    String line = myReader.nextLine() + "\n";
                    data += line;
                }
                //System.out.println(data);
                myReader.close();
                } catch (FileNotFoundException o) {
                System.out.println("An error occurred.");
                o.printStackTrace();
                }

                //write to file
                try {
                FileWriter myWriter = new FileWriter(detailsPath);
                if (user.equals("") || password.equals("")){
                    myWriter.write(data); 
                }
                else{
                    myWriter.write(data + user + ", " + password);
                    people.put(user,password);
                    System.out.println(user + ":" + password);
                }
                myWriter.close();
                System.out.println("Successfully wrote to the file.");
                } catch (IOException o) {
                System.out.println("An error occurred.");
                o.printStackTrace();
                }
            }
        }

        if (e.getSource()==Logout){
            Main.setVisible(false);
            frame.remove(Main); 
            
            reset();
            frame.add(Login);
            Login.setVisible(true);

            
        }
    
        if (e.getSource()==fontLeft){
            fontIndex += (fonts.length-1);
            fontIndex %= fonts.length;
            setFonts(Main);
            setFonts(Login);
        }
    
        if (e.getSource()==fontRight){
            fontIndex ++;
            fontIndex %= fonts.length;
            setFonts(Main);
            setFonts(Login);
        }
    }

    @Override
    public void mouseClicked(MouseEvent e) {
        // TODO Auto-generated method stub
        System.out.println(e.getX() + " : " + e.getY());
    }
    @Override
    public void mousePressed(MouseEvent e) {
        
    }
    @Override
    public void mouseReleased(MouseEvent e) {
       
    }
    @Override
    public void mouseEntered(MouseEvent e) {
       
    }
    @Override
    public void mouseExited(MouseEvent e) {
        
    }

    @Override
    public void stateChanged(ChangeEvent e) {
        Login.setBackground(new java.awt.Color(255-redSlider.getValue(),255-greenSlider.getValue(),255-blueSlider.getValue()));
        
    }
}