import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class InterfazGrafica extends JFrame {

    private JTextField codigoTextField;
    private JTextField montoRecargaTextField;
    private JButton recargarButton;
    private JTextArea resultadoTextArea;
    //Crea la interfaz
    public InterfazGrafica() {
        setTitle("Recarga de Tarjeta");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        JPanel panelEntrada = new JPanel();
        panelEntrada.setLayout(new GridLayout(3, 2));

        JLabel lblCodigo = new JLabel("Código de Tarjeta:");
        codigoTextField = new JTextField();
        JLabel montoLabel = new JLabel("Monto a Recargar:");
        montoRecargaTextField = new JTextField();
        recargarButton = new JButton("Recargar");

        panelEntrada.add(lblCodigo);
        panelEntrada.add(codigoTextField);
        panelEntrada.add(montoLabel);
        panelEntrada.add(montoRecargaTextField);
        panelEntrada.add(new JLabel()); // Espacio en blanco
        panelEntrada.add(recargarButton);

        resultadoTextArea = new JTextArea();
        resultadoTextArea.setEditable(false);

        add(panelEntrada, BorderLayout.NORTH);
        add(resultadoTextArea, BorderLayout.CENTER);

        recargarButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                String codigo = codigoTextField.getText();
                int montoRecarga = Integer.parseInt(montoRecargaTextField.getText());
                String nuevoCodigo = Funcionalidad.recargarSaldo(codigo, montoRecarga);
                resultadoTextArea.setText(nuevoCodigo);
            }
        });
    }
    //Corre la interfaz
    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                InterfazGrafica interfaz = new InterfazGrafica();
                interfaz.setVisible(true);
            }
        });
    }
}
