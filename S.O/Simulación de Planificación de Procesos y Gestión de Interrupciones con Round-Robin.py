import threading
import time


class Process:
    def __init__(self, name, bursts):
        self.name = name
        self.bursts = bursts
        self.current_burst = 0
        self.state = "ready"

    def execute(self):
        if self.current_burst < len(self.bursts):
            burst = self.bursts[self.current_burst]
            if burst == "CPU":
                self.execute_cpu()
            elif burst == "E/S":
                self.execute_io()

    def execute_cpu(self):
        print(f"Proceso {self.name}: Ejecutando en CPU")
        time.sleep(1)
        self.current_burst += 1
        if self.current_burst >= len(self.bursts):
            self.state = "terminated"

    def execute_io(self):
        print(f"Proceso {self.name}: Realizando operaciones de E/S")
        time.sleep(1)
        self.current_burst += 1
        if self.current_burst >= len(self.bursts):
            self.state = "terminated"


class Interrupt:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def execute(self):
        print(f"Interrupción {self.name}: Ejecutando rutina de tratamiento")
        time.sleep(1)


def run_rr_scheduler(processes, interrupts):
    current_time = 0
    current_process_index = 0
    current_interrupt_index = 0
    cpu_busy = False
    io_busy = False

    while True:
        if current_time % 5 == 0:
            if current_interrupt_index < len(interrupts):
                interrupt = interrupts[current_interrupt_index]
                interrupt.execute()
                current_interrupt_index += 1

        if not cpu_busy:
            process = processes[current_process_index]
            process.execute()
            if process.state == "terminated":
                current_process_index += 1
                if current_process_index >= len(processes):
                    break

        if not io_busy and current_process_index < len(processes):
            process = processes[current_process_index]
            if process.bursts[process.current_burst] == "E/S":
                print(f"Instante {current_time}: Dispositivo de E/S en uso")
                io_busy = True

        if io_busy:
            io_busy = False
            print(f"Instante {current_time}: Dispositivo de E/S liberado")

        current_time += 1
        time.sleep(0.1)


# Crear procesos
processes = [
    Process("A", ["CPU"] * 15),
    Process("B", ["CPU", "E/S", "CPU"] * 2),
    Process("C", ["CPU", "E/S", "CPU"] + ["E/S"] * 6 + ["CPU"] * 4)
]

# Crear interrupciones
interrupts = [
    Interrupt("IH", 0),
    Interrupt("IR", 1),
    Interrupt("IS", 2)
]

# Ejecutar el planificador Round-Robin
run_rr_scheduler(processes, interrupts)
