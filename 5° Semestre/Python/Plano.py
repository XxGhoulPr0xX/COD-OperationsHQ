import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

class ManufacturingProcess:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(10, 8))
        self.ancho = 10
        self.alto = 8
        self.ax.set_xlim(0, self.ancho)
        self.ax.set_ylim(0, self.alto)
        self.detector_patches = []
        self.detector_labels = ['Detector 1', 'Detector 2', 'Detector 3', 'Detector 4', 'Detector 5',
                                'Detector 6', 'Detector 7', 'Detector 8', 'Detector 9', 'Detector 10']
        self.detector_states = [False] * len(self.detector_labels)
        self.start_times = [0] * len(self.detector_labels)
        self.end_times = [0] * len(self.detector_labels)
        self.setup_zones()
        self.setup_detectors()
        self.setup_animation()

    def setup_zones(self):
        self.ax.add_patch(plt.Rectangle((0, 0), 3, 2, facecolor='lightblue', edgecolor='black'))
        self.ax.text(1.5, 1, 'Recepción de\nMaterias Primas', ha='center', va='center')

        self.ax.add_patch(plt.Rectangle((0, 3), 2, 3, facecolor='gray', edgecolor='black'))
        self.ax.text(1, 4.5, 'Almacenamiento de\nMaterias Primas', ha='center', va='center')

        self.ax.add_patch(plt.Rectangle((3, 0), 6, 8, facecolor='lightgreen', edgecolor='black'))
        self.ax.text(6, 4, 'Producción de\nJuguetes', ha='center', va='center')

        self.ax.add_patch(plt.Rectangle((3, 7), 6, 1, facecolor='orange', edgecolor='black'))
        self.ax.text(6, 7.5, 'Ensamblaje de\nJuguetes', ha='center', va='center')

        self.ax.add_patch(plt.Rectangle((3, 1), 6, 1, facecolor='yellow', edgecolor='black'))
        self.ax.text(6, 1.5, 'Embalaje de\nJuguetes', ha='center', va='center')

        self.ax.add_patch(plt.Rectangle((9, 0), 1, 8, facecolor='purple', edgecolor='black'))
        self.ax.text(9.5, 4, 'Almacenamiento de\nJuguetes Terminados', ha='center', va='center')

    def setup_detectors(self):
        detectores = [(1.5, 0.5), (1.5, 1.5), (1, 3.5), (1, 5.8), (7, 7.5), (7, 1.5), (9.5, 5), (4.5, 0.5), (4.5, 1.5), (8, 5)]
        for i, detector in enumerate(detectores):
            detector_patch = plt.Circle(detector, 0.15, facecolor='red', edgecolor='black')
            self.detector_patches.append(detector_patch)
            self.ax.add_patch(detector_patch)
            self.ax.text(detector[0], detector[1], self.detector_labels[i], ha='center', va='center')

    def setup_animation(self):
        self.animation = animation.FuncAnimation(self.fig, self.animate, frames=10, interval=500)

    def animate(self, frame):
        for i, patch in enumerate(self.detector_patches):
            if self.detector_states[i] and frame % 2 == 0:
                patch.set_alpha(1.0)
            else:
                patch.set_alpha(0.0)

    def activate_all_detectors(self):
        all_active = all(self.detector_states)
        for i, patch in enumerate(self.detector_patches):
            if not all_active:
                patch.set_alpha(1.0)
                if self.start_times[i] == 0:
                    self.start_times[i] = time.time()
                    print(f"Se activó el {self.detector_labels[i]}")
            else:
                patch.set_alpha(0.0)
                if self.end_times[i] == 0:
                    self.end_times[i] = time.time()
                    tiempo_total = self.end_times[i] - self.start_times[i]
                    print(f"Se apagó el {self.detector_labels[i]}")
                    print(f"Tiempo de encendido para {self.detector_labels[i]}: {tiempo_total/60} segundos")
        self.detector_states = [not all_active] * len(self.detector_labels)

    def activate_detector(self, event):
        if event.inaxes is not None:
            for i, patch in enumerate(self.detector_patches):
                if patch.contains(event)[0]:
                    if patch.get_alpha() == 0.0:
                        patch.set_alpha(1.0)
                        if self.start_times[i] == 0:
                            self.start_times[i] = time.time()
                            print(f"Se activó el {self.detector_labels[i]}")
                    else:
                        patch.set_alpha(0.0)
                        if self.end_times[i] == 0:
                            self.end_times[i] = time.time()
                            tiempo_total = self.end_times[i] - self.start_times[i]
                            print(f"Se apagó el {self.detector_labels[i]}")
                            print(f"Tiempo de encendido para {self.detector_labels[i]}: {tiempo_total/60} segundos")
                    self.detector_states[i] = not self.detector_states[i]
                    self.activate_all_detectors()

    def run(self):
        self.fig.canvas.mpl_connect('button_press_event', self.activate_detector)
        self.ax.axis('off')
        plt.show()

if __name__ == '__main__':
    process = ManufacturingProcess()
    process.run()
