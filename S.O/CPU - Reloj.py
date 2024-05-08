import threading
import time

# Definición de las constantes
QUANTUM = 2  # Quantum de dos interrupciones de reloj
INTERRUPTION_CLOCK = 5  # Unidades de tiempo para la interrupción de reloj

# Variables para controlar los procesos y las interrupciones
cpu_busy = False
processes = ["A", "B", "C"]
queue = processes.copy()
clock_count = 0
io_in_use = False

# Función para la rutina de tratamiento de la interrupción de reloj


def clock_interrupt():
    global cpu_busy, processes, queue, clock_count, io_in_use

    clock_count += 1
    print(f"Reloj: {clock_count}")

    if cpu_busy:
        if clock_count % QUANTUM == 0:
            queue.append(queue.pop(0))
            print(f"Proceso {queue[0]} pasa al final de la cola")

    if clock_count % INTERRUPTION_CLOCK == 0:
        if not cpu_busy:
            if io_in_use:
                print("Dispositivo de E/S en uso")
            else:
                if queue:
                    process = queue.pop(0)
                    if process == "A":
                        print("CPU atiende Proceso A")
                        # Simula el tiempo de ejecución del proceso A
                        time.sleep(15)
                    elif process == "B":
                        print("CPU atiende Proceso B")
                        # Simula el tiempo de ejecución del proceso B
                        time.sleep(2)
                        io_in_use = True
                        print("Dispositivo de E/S en uso")
                        time.sleep(1)  # Simula el tiempo de E/S
                        io_in_use = False
                        print("CPU continúa con Proceso B")
                        # Simula el resto del tiempo de ejecución del proceso B
                        time.sleep(3)
                    elif process == "C":
                        print("CPU atiende Proceso C")
                        # Simula el tiempo de ejecución del proceso C
                        time.sleep(1)
                        io_in_use = True
                        print("Dispositivo de E/S en uso")
                        time.sleep(6)  # Simula el tiempo de E/S
                        io_in_use = False
                        print("CPU continúa con Proceso C")
                        # Simula el resto del tiempo de ejecución del proceso C
                        time.sleep(4)
                    print(f"Proceso {process} finalizado")
                    cpu_busy = False

    if not cpu_busy:
        if queue:
            process = queue.pop(0)
            if process == "A":
                print("CPU atiende Proceso A")
                time.sleep(15)  # Simula el tiempo de ejecución del proceso A
            elif process == "B":
                print("CPU atiende Proceso B")
                time.sleep(2)  # Simula el tiempo de ejecución del proceso B
                io_in_use = True
                print("Dispositivo de E/S en uso")
                time.sleep(1)  # Simula el tiempo de E/S
                io_in_use = False
                print("CPU continua con Proceso B")
                # Simula el resto del tiempo de ejecución del proceso B
                time.sleep(3)
            elif process == "C":
                print("CPU atiende Proceso C")
                time.sleep(1)  # Simula el tiempo de ejecución del proceso C
                io_in_use = True
                print("Dispositivo de E/S en uso")
                time.sleep(6)  # Simula el tiempo de E/S
                io_in_use = False
                print("CPU continua con Proceso C")
                # Simula el resto del tiempo de ejecución del proceso C
                time.sleep(4)
            print(f"Proceso {process} finalizado")
            cpu_busy = False

# Función para iniciar el sistema


def start_system():
    while True:
        clock_interrupt()
        time.sleep(1)  # Espera de 1 unidad de tiempo


# Creación y arranque del hilo principal del sistema
system_thread = threading.Thread(target=start_system)
system_thread.start()
