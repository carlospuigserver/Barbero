import threading
import time
from barberiaa import Barberia
from barbero import Barbero
from clientee import Cliente

def main():
    barberia=Barberia(5)
    barbero= Barbero("Carlos",barberia)
    clientes= [Cliente(f"Cliente {i}",barberia) for i in range(10)]
    hilo_barbero=threading.Thread(target=barbero.trabajar)
    hilo_barbero.start()
    

    for cliente in clientes:
        cliente.visita()
        time.sleep(1)
    barberia.exit(barbero.nombre)

if __name__ == "__main__":
    main()
    

