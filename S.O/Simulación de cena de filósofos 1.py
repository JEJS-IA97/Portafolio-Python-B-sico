from threading import Thread, Lock, Condition
import time

class CenaFilosofos:
    def __init__(self, n, m):
        self.tenedores_disponibles = [True] * m
        self.max_comensales = n // 2
        self.comensales = 0
        self.arbitro = Arbitro(m)
        self.cond = Condition()

    def tomar_tenedores(self, filosofo):
        with self.cond:
            while not self.arbitro.tomar_tenedores(filosofo):
                self.cond.wait()
            print(f"Filósofo {filosofo} tomó los tenedores.")

    def liberar_tenedores(self, filosofo):
        with self.cond:
            self.arbitro.liberar_tenedores(filosofo)
            self.cond.notify_all()
            print(f"Filósofo {filosofo} liberó los tenedores.")

    def sentarse(self):
        with self.cond:
            while self.comensales >= self.max_comensales:
                self.cond.wait()
            self.comensales += 1
            print("Un filósofo se sentó a cenar.")

    def levantarse(self):
        with self.cond:
            self.comensales -= 1
            self.cond.notify_all()
            print("Un filósofo se levantó de la mesa.")

class Arbitro:
    def __init__(self, n):
        self.tenedores = [Lock() for i in range(n)]

    def tomar_tenedores(self, filosofo):
        if filosofo % 2 == 0:
            self.tenedores[filosofo].acquire()
            self.tenedores[(filosofo + 1) % len(self.tenedores)].acquire()
            return True
        else:
            self.tenedores[(filosofo + 1) % len(self.tenedores)].acquire()
            self.tenedores[filosofo].acquire()
            return True

    def liberar_tenedores(self, filosofo):
        self.tenedores[filosofo].release()
        self.tenedores[(filosofo + 1) % len(self.tenedores)].release()

def filosofo(id, cena):
    while True:
        cena.sentarse()
        cena.tomar_tenedores(id)
        comer()
        cena.liberar_tenedores(id)
        cena.levantarse()
        pensar()

def comer():
    print("El filósofo está comiendo...")
    time.sleep(1)  # Simulación de tiempo para comer

def pensar():
    print("El filósofo está pensando...")
    time.sleep(1)  # Simulación de tiempo para pensar

n = 5
m = n - 1

cena = CenaFilosofos(n, m)

filosofos = []
for i in range(n):
    filosofos.append(Thread(target=filosofo, args=(i, cena)))

print("Simulación de cena de filósofos iniciada.")

for f in filosofos:
    f.start()

for f in filosofos:
    f.join()

print("Simulación de cena de filósofos finalizada.")
