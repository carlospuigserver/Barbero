import threading
import time

class Barbero:
    def __init__(self, nombre,barberia):
        self.nombre=nombre
        self.barberia=barberia
    
    def trabajar(self):
        while True:
            if self.barberia.sillas.empty():
                print(f"{self.nombre} esta durmiendo")
            else:
                cliente=self.barberia.sillas.get()
                print(f"{self.nombre} esta cortando el pelo a {cliente}")
                time.sleep(3)
