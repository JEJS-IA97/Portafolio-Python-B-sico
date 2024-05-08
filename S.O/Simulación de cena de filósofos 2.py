from threading import Thread, Condition
import time

class CenaFilosofos:
    def __init__(self, n):
        self.tenedores_disponibles = [True] * n  # Inicializa los tenedores como disponibles
        self.cond = Condition()  # Crea un objeto Condition para gestionar el acceso a los tenedores

    # Operación para tomar los tenedores
    def tomar_tenedores(self, filosofo):
        with self.cond:  # Adquiere el lock del objeto Condition
            # Espera mientras los tenedores adyacentes estén ocupados
            while not self.tenedores_disponibles[filosofo] or not self.tenedores_disponibles[(filosofo + 1) % len(self.tenedores_disponibles)]:
                self.cond.wait()  # Libera el lock y espera a que se notifique
            # Marca los tenedores como no disponibles
            self.tenedores_disponibles[filosofo] = False
            self.tenedores_disponibles[(filosofo + 1) % len(self.tenedores_disponibles)] = False

    # Operación para liberar los tenedores
    def liberar_tenedores(self, filosofo):
        with self.cond:  # Adquiere el lock del objeto Condition
            # Marca los tenedores como disponibles
            self.tenedores_disponibles[filosofo] = True
            self.tenedores_disponibles[(filosofo + 1) % len(self.tenedores_disponibles)] = True
            self.cond.notify_all()  # Notifica a cualquier filósofo que esté esperando

# Función que representa el comportamiento de un filósofo
def filosofo(id, cena):
    while True:
        pensar(id)  # El filósofo piensa
        cena.tomar_tenedores(id)  # El filósofo toma los tenedores
        comer(id)  # El filósofo come
        cena.liberar_tenedores(id)  # El filósofo libera los tenedores

# Función que representa el comportamiento de pensar
def pensar(id):
    print(f"Filósofo {id} está pensando...\n")
    time.sleep(1)  # Simulación de tiempo para pensar

# Función que representa el comportamiento de comer
def comer(id):
    print(f"Filósofo {id} está comiendo...\n")
    time.sleep(1)  # Simulación de tiempo para comer

cena = CenaFilosofos(5)  # Crea una instancia de la clase CenaFilosofos con 5 tenedores

filosofos = []
for i in range(5):
    filosofos.append(Thread(target=filosofo, args=(i, cena)))  # Crea un hilo para cada filósofo

for f in filosofos:
    f.start()  # Inicia los hilos

for f in filosofos:
    f.join()  # Espera a que los hilos terminen
