import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;


public class GUI implements ActionListener{

    int clicks = 0;
    private JLabel label;
    private JButton button;
    private JFrame frame;
    private JPanel panel;
   

    public GUI(){
        //initialize panel and frame
        frame = new JFrame();
        panel = new JPanel();

        //set window size and other stuff
        panel.setBorder(BorderFactory.createEmptyBorder(30,30,10,30));
        panel.setLayout(new GridLayout(0,1));

        //add new elements
        button = new JButton("Click me");
        button.addActionListener(this);

        label = new JLabel("Number of clicks: 0");

        

        

       //add elements to panel
        panel.add(button);
        panel.add(label);

        //set frame
        frame.add(panel, BorderLayout.CENTER);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setTitle("Test GUI");
        frame.pack();
        frame.setVisible(true);
    }

    public static void main(String[] args){
        
        new GUI();
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        clicks++;
        label.setText("Number of clicks: " + clicks);
    }
}
