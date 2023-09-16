import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Practica1 extends JFrame 
    implements ActionListener {

    private JButton boton;
    private JPanel panel;

    public static void main(String[] args) {
        Practica1 marco = new Practica1();
        marco.setSize(400, 300);
        marco.crearGUI();
        marco.setVisible(true);
    }

    private void crearGUI() {
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        Container ventana = getContentPane();
        ventana.setLayout(new FlowLayout() );

	panel = new JPanel();
	panel.setPreferredSize(new Dimension(300, 200));
	panel.setBackground(Color.white);
	ventana.add(panel);

	boton = new JButton("Haga clic");
	ventana.add(boton);
	boton.addActionListener(this);
    }

    public void actionPerformed(ActionEvent event) {
        Graphics papel = panel.getGraphics();
	papel.drawLine(0, 0, 100, 100);
    }	
}