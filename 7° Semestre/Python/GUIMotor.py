import tkinter as tk
import random

class MotorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Teléfono de Avisos de Fallas del Motor")
        self.root.geometry("300x500")

        self.error_messages = [
            "Falla en el sistema de refrigeración.",
            "Fuga de aceite detectada.",
            "Sobrecalentamiento del motor.",
            "Baja presión de aceite.",
            "Problema en el sistema de combustible."
        ]

        self.phone_frame = tk.Frame(root, bg="black")
        self.phone_frame.pack(fill=tk.BOTH, expand=True)

        self.error_label = tk.Label(self.phone_frame, text="", font=("Arial", 14), bg="black", fg="white", wraplength=250)
        self.error_label.pack(pady=20)

        # Inicializar el temporizador para mostrar la primera falla después de 10 segundos
        self.root.after(10000, self.update_error_message)

    def update_error_message(self):
        error_message = random.choice(self.error_messages)
        self.error_label.config(text=error_message)

        # Cambiar el color de fondo basado en el tipo de falla
        if "refrigeración" in error_message:
            self.phone_frame.configure(bg="blue")
        elif "aceite" in error_message:
            self.phone_frame.configure(bg="red")
        elif "sobrecalentamiento" in error_message:
            self.phone_frame.configure(bg="orange")
        elif "presión de aceite" in error_message:
            self.phone_frame.configure(bg="yellow")
        else:
            self.phone_frame.configure(bg="white")

        # Programar la próxima actualización después de un tiempo aleatorio
        tiempo_aleatorio = random.randint(1, 100)
        self.root.after(tiempo_aleatorio * 1000, self.update_error_message)

def main():
    root = tk.Tk()
    app = MotorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
