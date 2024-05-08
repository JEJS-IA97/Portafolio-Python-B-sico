import subprocess
import click
from colorama import init, Fore, Style

init(autoreset=True)  # Inicializar colorama para que funcione en Windows

@click.command()
def main():
    while True:
        click.clear()
        print(f"{Fore.CYAN}==== Menú M/M/s ===={Style.RESET_ALL}")
        print(f"{Fore.YELLOW}1. {Fore.RESET}M/M/1 (Primera Versión)")
        print(f"{Fore.YELLOW}2. {Fore.RESET}M/M/1 (Segunda Versión)")
        print(f"{Fore.YELLOW}3. {Fore.RESET}M/M/S")
        print(f"{Fore.YELLOW}4. {Fore.RESET}M/M/S/K")
        print(f"{Fore.RED}5. {Fore.RESET}Salir")

        opcion = click.prompt(f"{Fore.GREEN}Seleccione una opción (1-5): {Style.RESET_ALL}", type=int)

        if opcion == 1:
            subprocess.run(["python", "MM1.py"])
        elif opcion == 2:
            subprocess.run(["python", "MM.py"])
        elif opcion == 3:
            subprocess.run(["python", "MMS.py"])
        elif opcion == 4:
            subprocess.run(["python", "MMSK.py"])
        elif opcion == 5:
            print(f"{Fore.RED}Saliendo del programa. ¡Hasta luego!{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Opción no válida. Por favor, elija una opción del 1 al 5.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
