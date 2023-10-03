import java.awt.*;
import javax.swing.*;

public class Practica4 extends JFrame {
    private JPanel panel;
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Practica4 marco = new Practica4();
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
                g.setColor(Color.WHITE);
                g.fillRect(50, 10, 10, 10);
                g.setColor(Color.BLUE);
                g.fillRect(50, 30, 10, 10);
                g.setColor(Color.CYAN);
                g.fillRect(50, 50, 10, 10);
                g.setColor(Color.DARK_GRAY);
                g.fillRect(50, 70, 10, 10);
                g.setColor(Color.GRAY);
                g.fillRect(70, 10, 10, 10);
                g.setColor(Color.GREEN);
                g.fillRect(70, 30, 10, 10);
                g.setColor(Color.LIGHT_GRAY);
                g.fillRect(70, 50, 10, 10);
                g.setColor(Color.MAGENTA);
                g.fillRect(70, 70, 10, 10);
                g.setColor(Color.ORANGE);
                g.fillRect(90, 10, 10, 10);
                g.setColor(Color.PINK);
                g.fillRect(90, 30, 10, 10);
                g.setColor(Color.RED);
                g.fillRect(90, 50, 10, 10);
                g.setColor(Color.YELLOW);
                g.fillRect(90, 70, 10, 10);
            }
        };
        panel.setPreferredSize(new Dimension(300, 200));
        panel.setBackground(Color.black);
        ventana.add(panel);
    }
}