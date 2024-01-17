import java.awt.*;
import javax.swing.*;

public class Practica3U2 extends JFrame {
    private JPanel panel;
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Practica3U2 marco = new Practica3U2();
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
                g.setColor(Color.BLUE);
                g.drawLine(0, 0, 10, 200);
                g.drawLine(0,10,20,200);
                g.drawLine(0,20,30,200);
                g.drawLine(0,30,40,200);
                g.drawLine(0, 40, 50, 200);
                g.drawLine(0, 50, 60, 200);
                g.drawLine(0,60,70,200);
                g.drawLine(0, 70, 80, 200);
                g.drawLine(0,80,90,200);
                g.drawLine(0,90,100,200);
                g.drawLine(0,100,110,200);
                g.drawLine(0,110,120,200);
                g.drawLine(0,120,130,200);
                g.drawLine(0,130,140,200);
                g.drawLine(0,140,150,200);
                g.drawLine(0,150,160,200);
                g.drawLine(0,160,170,200);
                g.drawLine(0,170,180,200);
                g.drawLine(0,180,190,200);
                g.drawLine(0,190,200,200);
                g.setColor(Color.pink);
                g.drawLine(0, 110, 100, 0);
                g.drawLine(0,100,110,0);
                g.drawLine(0,90,120,0);
                g.drawLine(0,80,130,0);
                g.drawLine(0, 70, 140, 0);
                g.drawLine(0, 60, 150, 0);
                g.drawLine(0,50,160,0);
                g.drawLine(0, 40, 170, 0);
                g.drawLine(0,30,180,0);
                g.drawLine(0,20,190,0);
                g.drawLine(0,10,200,0);
            }
        };
        panel.setPreferredSize(new Dimension(300, 200));
        panel.setBackground(Color.black);
        ventana.add(panel);
    }
}