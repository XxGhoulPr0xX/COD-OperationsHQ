import java.awt.*;
import javax.swing.*;

public class Practica1U2 extends JFrame {
    private JPanel panel;
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Practica1U2 marco = new Practica1U2();
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
                int x[]={170,90,110,80,20,15};
                int y[]={100,100,110,110,80,60};

                int x1[]={0,10,20,30,40,50};
                int y1[]={0,20,30,40,50,60};

                int x2[]={190,110,130,110,40,15};
                int y2[]={130,130,130,130,100,60};
                g.setColor(Color.BLUE);
                g.fillPolygon(x1, y1, 3);
                g.setColor(Color.red);
                g.fillPolygon(x2, y2, 5);
                g.setColor(Color.GREEN);
                g.fillPolygon(x, y, 4);
            }
        };
        panel.setPreferredSize(new Dimension(300, 200));
        panel.setBackground(Color.white);
        ventana.add(panel);
    }
}