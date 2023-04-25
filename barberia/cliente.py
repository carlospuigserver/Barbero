import threading
import time

class cliete:
    def __init__(self, nombre,barberia):
        self.nombre=nombre
        self.barberia=barberia

    def visita(self):
        self.barberia.entrar(self.nombre)