import os
import sys
import subprocess
from pathlib import Path

def menu():
    print("1. Iniciar servidor")
    print("2. Iniciar cliente")
    print("3. Salir")
    opcion = input("Ingrese una opcion: ")
    return opcion

if __name__ == '__main__':
    os.system("cls")
    while True:
        
        opcion = menu()
        match opcion:
            case "1":
                os.system("cls")
                tcp_server_path = Path(__file__).parent / "TCP_Server.py"
                subprocess.Popen(['start', 'cmd', '/k', f'python {tcp_server_path}'], shell=True)
            case "2":
                os.system("cls")
                print("--- Cliente TCP ---")
                num=input("Cuantos clientes deseas conectar?: ")
                for i in range(int(num)):
                    tcp_client_path = Path(__file__).parent / "TCP_Client.py"
                    subprocess.Popen(['start', 'cmd', '/k', f'python {tcp_client_path}'], shell=True)
            case "3":
                sys.exit()
            case _:
                print("Opción no válida")
    

