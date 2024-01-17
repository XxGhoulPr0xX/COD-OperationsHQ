import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Game extends JPanel {

	int x = 0;
	int y = 180;
	int y1= 190;
	int x1= 10;

	private void Suma() {
		x = x + 1;
		x1 = x1+1;
	}

	@Override
	public void paint(Graphics g) {
		super.paint(g);
		g.setColor(Color.cyan);
		g.fillRect(0, 0, 400, 300);
		g.setColor(Color.green);
		g.fillRect(0, 180, 400, 100);
		g.setColor(Color.YELLOW);
		g.fillOval(10,10,50,50);
		g.setColor(Color.RED);
		g.fillRect(100, 98, 100, 100);
		g.setColor(Color.DARK_GRAY);
		g.fillRect(130, 148, 30, 50);
		g.setColor(Color.BLUE);
		g.fillOval(105,110,30,30);
		g.fillOval(165,110, 30, 30);
		g.setColor(Color.BLACK);
		g.fillRect(80, 38, 145, 60);
		g.fillArc(80, 14, 145, 60, 0, 180);
		g.setColor(Color.BLACK);
		g.fillOval(130,170,10,10);
		g.setColor(Color.YELLOW);
		g.fillArc(x, y, 50, 50, 0, -300);
		g.setColor(Color.BLACK);
		g.fillOval(x1, y1, 10, 10);

	}

	public static void main(String[] args) throws InterruptedException {
		JFrame frame = new JFrame("Pac-Man House");
		Game game = new Game();
		frame.add(game);
		frame.setSize(300, 300);
		frame.setVisible(true);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		int i=0;
		while (i<=300) {
			game.Suma();
			game.repaint();
			Thread.sleep(10);
			i++;
		}
	}
}