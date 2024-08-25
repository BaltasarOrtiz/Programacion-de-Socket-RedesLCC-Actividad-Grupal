import socket
from time import ctime
import threading

HOST = 'localhost'
PORT = 21567

def handle_client(client_sock, addr):
    try:
        print('Informacion recibida desde el cliente: ', client_sock.recv(1024).decode('utf-8'))
        client_sock.send('\nHola soy el servidor "{}:{}" '.format(HOST,PORT).encode('utf-8'))
        while True:
            client_sock.send('\n----Menu----\n1. Realizar operación\n2. Obtener hora del servidor\n3. Salir\n------------\n'.encode('utf-8'))
            opcion = client_sock.recv(1024).decode('utf-8')

            if opcion == '1':
                operacion = client_sock.recv(1024).decode('utf-8')
                try:
                    resultado = eval(operacion)
                except Exception as e:
                    resultado = f'Error: {e}'
                client_sock.send(f'Respuesta [{resultado}]'.encode('utf-8'))
            elif opcion == '2':
                client_sock.send(f'La hora del servidor es: {ctime()}'.encode('utf-8'))
            elif opcion == '3':
                print(f'Conexión cerrada con {addr}')
                break
            else:
                client_sock.send('Opción no válida'.encode('utf-8'))
    except Exception as e:
        print('Error:', e)
    finally:
        client_sock.close()



def tcp_server():
    ADDR = (HOST, PORT)  # dirección de conexión
    try:
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea un socket de conexión
        server_sock.bind(ADDR)  # Asigna la dirección al socket
        server_sock.listen(5)  # Escucha hasta 5 conexiones
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reutiliza la dirección
        print('Esperando conexión...')
        while True:
            client_sock, addr = server_sock.accept()  # Acepta la conexión, diseño bloqueante
            client_thread = threading.Thread(target=handle_client, args=(client_sock, addr)) # Crea un nuevo hilo para manejar la conexión del cliente
            client_thread.start()
    except Exception as e:
        print('Error', e)
        return

    server_sock.close()  # Cierra el socket del servidor
        

if __name__ == '__main__':
    tcp_server()

