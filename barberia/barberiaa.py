import queue
import threading
import time

class Barberia:
    def __init__(self,Numsillas):
        self.NumSillas=Numsillas
        self.sillas=queue.Queue(Numsillas)

    def entrar(self, cliente):
        if self.sillas.full():
            print(f"{cliente} dice : La berbería está llena, vuelvo luego")
        else:
            self.sillas.put(cliente)
            print(f"{cliente} dice: Me siento en la silla a esperar")


    def salir(self, nombre_barbero):
        print(f"{nombre_barbero} se va a casa")
