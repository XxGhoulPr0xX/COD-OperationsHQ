import java.awt.*;
import javax.swing.*;

public class Practica3 extends JFrame {
    private JPanel panel;
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Practica3 marco = new Practica3();
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
                g.drawRect(100, 98, 100, 100);
                g.drawRect(130, 148, 30, 50);
                g.drawOval(105,110,30,30);
                g.drawOval(165,110, 30, 30);
                g.drawLine(80,98,220,98);
                g.drawLine(220,98,150,18);
                g.drawLine(150,18,80,98);
                g.drawLine(0,178,100,178);
                g.drawLine(200,178,300,178);
                g.drawOval(130,170,10,10);
                g.setColor(Color.YELLOW);
                g.drawOval(10,10,50,50);
            }
        };
        panel.setPreferredSize(new Dimension(300, 200));
        panel.setBackground(Color.white);
        ventana.add(panel);
    }
}

