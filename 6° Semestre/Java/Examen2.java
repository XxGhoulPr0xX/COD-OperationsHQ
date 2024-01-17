import java.awt.*;
import javax.swing.*;

public class Examen2 extends JFrame {
    private JPanel panel;
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Examen2 marco = new Examen2();
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
                g.setColor(Color.white);
                g.fillArc(20, 10, 50, 50, 0, 180);
                g.fillRect(20, 40, 50, 50);
                g.fillArc(20, 80, 50, 20, 180, 180);
                g.fillRect(30, 95, 10, 30);
                g.fillRect(50, 95, 10, 30);
                g.fillArc(30, 120, 10, 10, 180, 180);
                g.fillArc(50, 120, 10, 10, 180, 180);
                g.fillRect(5, 45, 10, 40);
                g.fillRect(75, 45, 10, 40);
                g.fillArc(5, 40, 10, 10, 0, 180);
                g.fillArc(75, 40, 10, 10, 0, 180);
                g.fillArc(5, 80, 10, 10, 180, 180);
                g.fillArc(75, 80, 10, 10, 180, 180);
                g.setColor(Color.BLACK);
                g.fillOval(30, 20, 5, 5);
                g.fillOval(55, 20, 5, 5);
                g.setColor(Color.WHITE);
                g.drawLine(30, 15, 20, 10);
                g.drawLine(60, 15, 70, 10);
            }
        };
        panel.setPreferredSize(new Dimension(300, 200));
        panel.setBackground(Color.black);
        ventana.add(panel);
    }
}