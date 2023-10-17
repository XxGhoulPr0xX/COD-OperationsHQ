import java.awt.*;
import javax.swing.*;

public class Practica6 extends JFrame {
    private JPanel panel;
    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Practica6 marco = new Practica6();
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
                int a=10;
                g.setColor(Color.DARK_GRAY);
                for(int i=1;i<=18;i++){
                    g.fillRect(10, a*i, a, a);
                    g.fillRect(280, a*i, a, a);
                }
                for(int i=1;i<=28;i++){
                    g.fillRect(a*i, 10, a, a);
                    g.fillRect(a*i, 180, a, a);
                }
                g.setColor(Color.green);
                for (int j = 0; j <= 8; j++) {
                    for (int i = 0; i <= 15 - j * 2; i++) {
                        int x = 20 + 10 * i;
                        int y = 20 + 20 * j + 10 * i;
                        g.fillRect(x, y, a, a);
                    }
                }
                g.setColor(Color.white);
                for(int i=0;i<=15;i++){
                    int x = 40 + 10 * i;
                    int y = 20 + 10 * i;
                    g.fillRect(x, y, a, a);
                }
                for(int i=0;i<=15;i++){
                    int x = 60 + 10 * i;
                    int y = 20 + 10 * i;
                    g.fillRect(x, y, a, a);
                }
                for(int i=0;i<=15;i++){
                    int x = 80 + 10 * i;
                    int y = 20 + 10 * i;
                    g.fillRect(x, y, a, a);
                }
                for(int i=0;i<=15;i++){
                    int x = 100 + 10 * i;
                    int y = 20 + 10 * i;
                    g.fillRect(x, y, a, a);
                }
                for(int i=0;i<=15;i++){
                    int x = 120 + 10 * i;
                    int y = 20 + 10 * i;
                    g.fillRect(x, y, a, a);
                }
                g.setColor(Color.RED);
                for(int i=0;i<=13;i++){
                    int x = 140 + 10 * i;
                    int y = 20 + 10 * i;
                    g.fillRect(x, y, a, a);
                }
                for(int i=0;i<=11;i++){
                    int x = 160 + 10 * i;
                    int y = 20 + 10 * i;
                    g.fillRect(x, y, a, a);
                }
                for(int i=0;i<=9;i++){
                    int x = 180 + 10 * i;
                    int y = 20 + 10 * i;
                    g.fillRect(x, y, a, a);
                }
                for(int i=0;i<=7;i++){
                    int x = 200 + 10 * i;
                    int y = 20 + 10 * i;
                    g.fillRect(x, y, a, a);
                }
                for(int i=0;i<=5;i++){
                    int x = 220 + 10 * i;
                    int y = 20 + 10 * i;
                    g.fillRect(x, y, a, a);
                }
                for(int i=0;i<=3;i++){
                    int x = 240 + 10 * i;
                    int y = 20 + 10 * i;
                    g.fillRect(x, y, a, a);
                }
                for(int i=0;i<=1;i++){
                    int x = 260 + 10 * i;
                    int y = 20 + 10 * i;
                    g.fillRect(x, y, a, a);
                }
            }
        };
        panel.setPreferredSize(new Dimension(300, 200));
        panel.setBackground(Color.black);
        ventana.add(panel);
    }
}