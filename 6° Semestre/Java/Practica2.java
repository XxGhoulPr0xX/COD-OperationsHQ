import java.awt.*;
import javax.swing.*;

public class Practica2 extends JFrame {
    private JPanel panel;
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Practica2 marco = new Practica2();
            marco.setSize(400, 300);
            marco.crearGUI();
            marco.setVisible(true);
        });
    }
    private void crearGUI() {
        Container ventana = getContentPane();
        ventana.setLayout(new FlowLayout());
        panel = new JPanel() {
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                g.drawLine(50, 50, 100, 50);
                g.drawLine(50, 50, 100, 100);
                g.drawLine(100, 100, 100, 150);
                g.drawLine(100, 150, 150, 100);
                g.drawLine(150,100,200,150);
                g.drawLine(200,150,200,100);
                g.drawLine(200,100,250,50);
                g.drawLine(250,50,200,50);
                g.drawLine(200,50,150,0);
                g.drawLine(150,0,100,50);
            }
        };
        panel.setPreferredSize(new Dimension(300, 200));
        panel.setBackground(Color.white);
        ventana.add(panel);
    }
}

