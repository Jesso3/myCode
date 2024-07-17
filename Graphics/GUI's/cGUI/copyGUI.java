import javax.swing.*;
import java.awt.*;


public class copyGUI{ //change name

    private JFrame frame;
    private JPanel panel;
   

    public copyGUI(){ //change name
        //initialize panel and frame
        frame = new JFrame();
        panel = new JPanel();

        //set window size and other stuff
        panel.setBorder(BorderFactory.createEmptyBorder(10,10,300,500));

        //make elements

        //add elements to panel
        
        //set frame
        frame.add(panel, BorderLayout.CENTER);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("Test GUI");
        frame.pack();
        frame.setVisible(true);
    }

    public static void main(String[] args){
        
        new copyGUI(); //change name
    }
}
