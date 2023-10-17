import tkinter as tk
from Funcionalidad import Funcionalidad

class InterfazGrafica(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Recarga de Tarjeta")
        self.geometry("400x300")
        self.alpha = Funcionalidad()  # Crear una instancia de Funcionalidad

        self.codigo_label = tk.Label(self, text="Código de Tarjeta:")
        self.codigo_label.grid(row=0, column=0, padx=10, pady=10)
        self.codigo_entry = tk.Entry(self)
        self.codigo_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.monto_label = tk.Label(self, text="Monto a Recargar:")
        self.monto_label.grid(row=1, column=0, padx=10, pady=10)
        self.monto_entry = tk.Entry(self)
        self.monto_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.recargar_button = tk.Button(self, text="Recargar", command=self.recargar)
        self.recargar_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        self.resultado_text = tk.Text(self, wrap=tk.WORD, width=40, height=10)
        self.resultado_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        self.resultado_text.config(state=tk.DISABLED)
    
    def recargar(self):
        codigo = self.codigo_entry.get()
        monto_recarga = self.monto_entry.get()

        if not codigo or not monto_recarga:
            self.resultado_text.config(state=tk.NORMAL)
            self.resultado_text.delete("1.0", tk.END)
            self.resultado_text.insert(tk.END, "Falta ingresar el código o el monto de recarga.")
            self.resultado_text.config(state=tk.DISABLED)
            return
        monto_recarga = int(monto_recarga)
        nuevo_codigo = self.alpha.recargarSaldo(codigo, monto_recarga)
        self.resultado_text.config(state=tk.NORMAL)
        self.resultado_text.delete("1.0", tk.END)
        self.resultado_text.insert(tk.END, nuevo_codigo)
        self.resultado_text.config(state=tk.DISABLED)

if __name__ == "__main__":
    app = InterfazGrafica()
    app.mainloop()
