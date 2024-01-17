import java.awt.*;
import javax.swing.*;

public class Practica2U2 extends JFrame {
    private JPanel panel;
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Practica2U2 marco = new Practica2U2();
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
                g.setColor(Color.RED);
                g.fillRect(100, 98, 100, 100);
                g.setColor(Color.DARK_GRAY);
                g.fillRect(130, 148, 30, 50);
                g.setColor(Color.BLUE);
                g.fillOval(105,110,30,30);
                g.fillOval(165,110, 30, 30);
                g.setColor(Color.WHITE);
                g.fillRect(80, 38, 145, 60);
                g.fillArc(80, 14, 145, 60, 0, 180);
                g.setColor(Color.BLACK);
                g.fillOval(130,170,10,10);
                g.setColor(Color.GRAY);
                g.fillOval(10,10,50,50);
            }
        };
        panel.setPreferredSize(new Dimension(300, 200));
        panel.setBackground(Color.BLACK);
        ventana.add(panel);
    }
}

