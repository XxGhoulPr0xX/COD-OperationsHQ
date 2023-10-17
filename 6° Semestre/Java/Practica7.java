import java.awt.*;
import javax.swing.*;

public class Practica7 extends JFrame {
    private JPanel panel;
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Practica7 marco = new Practica7();
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
                g.setColor(Color.YELLOW);
                g.fillArc(0, 0, 50, 50, 0, -300);
                g.fillArc(0, 60, 50, 50, 0, -270);
                g.fillArc(0, 110, 50, 50, 0, -230);
                g.fillArc(60, 0, 50, 50, 0, -180);
                g.fillArc(60, 60, 50, 50, -210, 60);
                g.fillArc(60, 110, 50, 50, 0, 360);
                g.setColor(Color.BLACK);
                g.fillOval(10, 10, 10, 10);
                g.fillOval(10, 70, 10, 10);
                g.fillOval(5, 120, 10, 10);
                g.fillOval(70, 30, 10, 10);
                g.fillOval(70, 80, 10, 10);
                g.fillOval(65, 120, 10, 10);
            }
        };
        panel.setPreferredSize(new Dimension(300, 200));
        panel.setBackground(Color.white);
        ventana.add(panel);
    }
}