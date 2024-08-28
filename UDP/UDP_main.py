import os
import sys
import subprocess
from pathlib import Path

def menu():
    print("UDP")
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
                udp_server_path = Path(__file__).parent / "UDP_Server.py"
                subprocess.Popen(['start', 'cmd', '/k', f'python {udp_server_path}'], shell=True)
            case "2":
                os.system("cls")       
                udp_client_path = Path(__file__).parent / "UDP_Client.py"
                subprocess.Popen(['start', 'cmd', '/k', f'python {udp_client_path}'], shell=True)
                os.system("cls")
            case "3":
                sys.exit()
            case _:
                print("Opción no válida")