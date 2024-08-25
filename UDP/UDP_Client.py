import time
import socket
import threading

HOST = 'localhost'
PORT = 12345

def cliente_udp():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    client_socket.settimeout(10)

    try:
        while True:
            print("\n--- Menú ---")
            print("1. Obtener hora del servidor")
            print("2. Realizar operacion: ")
            print("3. Salir")
            opcion = input("Elige una opción: ")

            if opcion == '1':
                # Enviar solicitud para obtener la hora
                mensaje = 'HORA'
                client_socket.sendto(mensaje.encode('utf-8'), (HOST, PORT))
                data, server = client_socket.recvfrom(1024)
                print(data.decode('utf-8'))
            elif opcion == '2':
                # Solicitar la operacion
                operacion = input("Ingrese la operacion: ")
                mensaje = f'OPERACION {operacion}'
                client_socket.sendto(mensaje.encode('utf-8'), (HOST,PORT))
                data, server = client_socket.recvfrom(1024)
                print(data.decode('utf-8'))
            elif opcion == '3':
                break
            else:
                print("Opción no válida, intenta de nuevo.")
    
    except socket.timeout:
        print("Error: Tiempo de espera agotado.")
    finally:
        client_socket.close()

if __name__ == "__main__":
    cliente_udp()