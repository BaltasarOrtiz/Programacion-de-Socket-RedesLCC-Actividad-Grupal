import time
import socket
import threading


def cliente_udp():
    HOST = input("Ingrese la dirección del host: ")
    PORT = int(input("Ingrese el puerto: "))
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        client_socket.settimeout(10)

        while True:
            print("\n--- Menú ---")
            print("1. Obtener hora del servidor")
            print("2. Realizar operacion: ")
            print("3. Salir")
            opcion = input("Elige una opción: ")

            if opcion == '1':
                mensaje = 'HORA'
                client_socket.sendto(mensaje.encode('utf-8'), (HOST, PORT))
                data, server = client_socket.recvfrom(1024)
                print(data.decode('utf-8'))
            elif opcion == '2':
                operacion = input("Ingrese la operacion: ")
                mensaje = f'OPERACION {operacion}'
                client_socket.sendto(mensaje.encode('utf-8'), (HOST,PORT))
                data, server = client_socket.recvfrom(1024)
                print(data.decode('utf-8'))
            elif opcion == '3':
                break
            else:
                print("Opción no válida, intenta de nuevo.")
    except Exception as e:
        print(f"Ha ocurrido un error: {e}")
    finally:
        client_socket.close()
        return

if __name__ == "__main__":
    cliente_udp()