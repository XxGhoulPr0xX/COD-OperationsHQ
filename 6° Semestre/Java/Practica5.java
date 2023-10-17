import java.awt.*;
import javax.swing.*;

public class Practica5 extends JFrame {
    private JPanel panel;
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Practica5 marco = new Practica5();
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
                int alturaY= 70;
                int anchuraX= 60;
                g.setColor(Color.BLUE);
                g.drawLine(60, 80, 60, 80+alturaY);
                g.drawLine(60, 80+alturaY, 60+anchuraX, 80+alturaY);
                g.drawLine(60, 80, 60+anchuraX, 80+alturaY);
                g.setColor(Color.WHITE);
                g.drawLine(80, 100, 80, 100+alturaY);
                g.drawLine(80, 100+alturaY, 80+anchuraX, 100+alturaY);
                g.drawLine(80, 100, 80+anchuraX, 100+alturaY);
                g.setColor(Color.RED);
                g.drawLine(100, 120, 100, 120+alturaY);
                g.drawLine(100, 120+alturaY, 100+anchuraX, 120+alturaY);
                g.drawLine(100, 120, 100+anchuraX, 120+alturaY);
            }
        };
        panel.setPreferredSize(new Dimension(300, 200));
        panel.setBackground(Color.black);
        ventana.add(panel);
    }
}