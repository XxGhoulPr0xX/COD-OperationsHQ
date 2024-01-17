import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class Juego:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Pantalla de carga")
        self.ventana.geometry("400x200")

        self.lblCargando = tk.Label(self.ventana, text="Cargando...")
        self.lblCargando.grid(row=1, column=1, padx=135, pady=5)

        self.ventana.style = ttk.Style()
        self.ventana.style.configure('Green.Horizontal.TProgressbar', troughcolor='green', background='green', thickness=20)
        self.pbCarga = ttk.Progressbar(self.ventana, length=300, mode='determinate', style='Green.Horizontal.TProgressbar')
        self.pbCarga.grid(row=2, column=1, pady=5)

        self.btnJugar = tk.Button(self.ventana, text="Jugar", command=self.getGame, state=tk.DISABLED)
        self.btnJugar.grid(row=3, column=1, padx=135, pady=5)

        self.ventana.after(500, self.goBar)

        self.shooting_enabled = True

        self.shoot_speed = 15
        self.puntuacion_jugador1 = 0
        self.puntuacion_jugador2 = 0
        self.setGalindoImagen = self.setImagen("Python\Juego\galindo.png")
        self.setDracoImagen = self.setImagen("Python\Juego\draco1.png")
        self.fondo_img = self.setImagenBackground("Python\Juego\Stage.jpg")  # Cambia la ruta a la ubicación de tu imagen

    def goBar(self):
        self.pbCarga["value"] = 0
        self.pbCarga.start(20)  
        self.ventana.after(3000, self.stopBar)

    def stopBar(self):
        self.pbCarga.stop()
        self.pbCarga["value"] = 100  # Llena la barra de progreso hasta el 100%
        self.btnJugar.config(state=tk.NORMAL)

    def setImagen(self, file_path):
        image = Image.open(file_path)
        new_width = int(image.width * 0.05)
        new_height = int(image.height * 0.05)
        image = image.resize((new_width, new_height), Image.LANCZOS)
        return ImageTk.PhotoImage(image)

    def setImagenBackground(self, file_path):
        image = Image.open(file_path)
        new_width = 1000
        new_height = 500
        image = image.resize((new_width, new_height), Image.LANCZOS)
        self.fondo_img = ImageTk.PhotoImage(image)
        return self.fondo_img

    def getGame(self):
        self.ventana.withdraw()  # Oculta la ventana principal en lugar de destruirla
        self.tlPantalla = tk.Toplevel(self.ventana)
        self.tlPantalla.title("Galindo vs Draco")
        self.tlPantalla.geometry("1000x600")

        self.cTablero = tk.Canvas(self.tlPantalla, width=1000, height=40, bg="black")
        self.cTablero.pack()

        self.lblJugador1 = tk.Label(self.cTablero, text=f"Jugador 1: {self.puntuacion_jugador1}", bg="white")
        self.lblJugador1.grid(row=0, column=0, padx=220, pady=10)

        self.lblJugador2 = tk.Label(self.cTablero, text=f"Jugador 2: {self.puntuacion_jugador2}", bg="white")
        self.lblJugador2.grid(row=0, column=1, padx=220, pady=10)

        btnVerde = tk.Button(self.cTablero, command=self.cargarTiempoReal, bg="green", width=10, height=2)
        btnVerde.grid(row=1, column=1, padx=5, pady=5)

        btnRojo = tk.Button(self.cTablero, command=self.cerrarConexion, bg="red", width=10, height=2)
        btnRojo.grid(row=1, column=0, padx=5, pady=5)
        self.cargarFondo()
        self.cargarGalindo()
        self.cargarDraco()

    def cargarFondo(self):
        self.cPantallaPrincipal = tk.Canvas(self.tlPantalla, width=1000, height=500)
        self.cPantallaPrincipal.pack()
        self.cPantallaPrincipal.create_image(0, 0, anchor=tk.NW, image=self.fondo_img)

    def cargarGalindo(self):
        self.galindoObjeto = self.cPantallaPrincipal.create_image(50, 250, anchor=tk.NW, image=self.setGalindoImagen)
        self.movimientoGalindo()

    def movimientoGalindo(self):
        self.tlPantalla.bind("<Right>", lambda event: (self.disparoGalindo(self.galindoObjeto)))
        self.tlPantalla.bind("<KeyPress-Up>", lambda event: self.moverGalindo(self.galindoObjeto, -50))
        self.tlPantalla.bind("<KeyPress-Down>", lambda event: self.moverGalindo(self.galindoObjeto, 50))

    def cargarDraco(self):
        self.dracoObjeto = self.cPantallaPrincipal.create_image(800, 250, anchor=tk.NW, image=self.setDracoImagen)
        self.movimiendoDraco()

    def movimiendoDraco(self):
        self.tlPantalla.bind("<KeyPress-w>", lambda event: self.moverDraco(self.dracoObjeto, -50))
        self.tlPantalla.bind("<KeyPress-s>", lambda event: self.moverDraco(self.dracoObjeto, 50))
        self.tlPantalla.bind("<KeyPress-a>", lambda event: self.disparoDraco(self.dracoObjeto))

    def moverGalindo(self, cuadrado, dy):
        x, y = self.cPantallaPrincipal.coords(cuadrado)
        nuevo_y = y + dy
        if 0 <= nuevo_y <= 350:
            self.cPantallaPrincipal.coords(cuadrado, x, nuevo_y)
            
    def moverDraco(self, cuadrado, dy):
        x1, y1 = self.cPantallaPrincipal.coords(cuadrado)
        nuevo_y = y1 + dy
        if 0 <= nuevo_y <= 350:
            self.cPantallaPrincipal.coords(cuadrado, x1, nuevo_y)

    def disparoGalindo(self, cuadrado):
        if self.shooting_enabled:
            self.shooting_enabled = False  # Cambiado a False para permitir ambos disparos simultáneamente
            x, y = self.cPantallaPrincipal.coords(cuadrado)
            shot = self.cPantallaPrincipal.create_rectangle(x, y, x + 20, y + 20, fill="red")
            self.direccionDisparoGalindo(shot, x)
            
    def direccionDisparoGalindo(self, shot, x):
        self.cPantallaPrincipal.move(shot, self.shoot_speed, 0)
        if self.cPantallaPrincipal.coords(shot)[2] < 1000:
            self.ventana.after(10, lambda: self.direccionDisparoGalindo(shot, x))
        else:
            self.cPantallaPrincipal.delete(shot)
            self.shooting_enabled = True
            self.verificar_colision(self.dracoObjeto,self.galindoObjeto, self.lblJugador1)

    def disparoDraco(self, cuadrado):
        if self.shooting_enabled:
            self.shooting_enabled = False  # Cambiado a False para permitir ambos disparos simultáneamente
            x2, y2 = self.cPantallaPrincipal.coords(cuadrado)
            shot = self.cPantallaPrincipal.create_rectangle(x2, y2, x2 - 20, y2 + 20, fill="purple")
            self.direccionDisparoDraco(shot, x2)

    def direccionDisparoDraco(self, shot, x2):
        self.cPantallaPrincipal.move(shot, -self.shoot_speed, 0)  # Cambié el signo de la velocidad
        if self.cPantallaPrincipal.coords(shot)[2] > 0:
            self.ventana.after(10, lambda: self.direccionDisparoDraco(shot, x2))
        else:
            self.cPantallaPrincipal.delete(shot)
            self.shooting_enabled = True
            self.verificar_colision(self.dracoObjeto,self.galindoObjeto, self.lblJugador2)

    def posicionActual(self, cuadrado):
        x,yG=self.cPantallaPrincipal.coords(cuadrado)
        return yG

    def verificar_colision(self, cuadradoD, cuadradoG, label_puntuacion):
        posicionGalindo=self.posicionActual(cuadradoG)
        posicionDraco=self.posicionActual(cuadradoD)
        if posicionDraco==posicionGalindo:
            self.aumentar_puntuacion(label_puntuacion)

    def aumentar_puntuacion(self, label_puntuacion):
        if label_puntuacion == self.lblJugador1:
            self.puntuacion_jugador1 += 1
        else:
            self.puntuacion_jugador2 += 1
        label_puntuacion.destroy()
        nuevo_label = tk.Label(self.cTablero, text=f"Jugador 1: {self.puntuacion_jugador1}" if label_puntuacion == self.lblJugador1 else f"Jugador 2: {self.puntuacion_jugador2}", bg="white")
        nuevo_label.grid(row=0, column=0 if label_puntuacion == self.lblJugador1 else 1, padx=220, pady=10)

    def MovimientoOnline(self, nueva_posicion):
        if nueva_posicion=="Arriba":
            self.moverGalindo(self.galindoObjeto, -50)
        if nueva_posicion=="Abajo":
            self.moverGalindo(self.galindoObjeto,50)
        if nueva_posicion=="Derecha":
            self.disparoGalindo(self.galindoObjeto)

    def cerrarConexion(self):
        messagebox.showerror("Exito","Se ha cerrado la conexion")

    def cargarTiempoReal(self):
        messagebox.showerror("Exito","Se ha actualizado la conexion")

    def run(self):
        self.ventana.mainloop()

if __name__=="__main__":
    charlie=Juego()
    charlie.run()