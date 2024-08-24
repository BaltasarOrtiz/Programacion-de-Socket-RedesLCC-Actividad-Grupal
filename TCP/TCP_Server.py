import socket
from time import ctime
import threading

def handle_client(client_sock, addr):
    BUFSIZ = 1024  # Tamaño de los paquetes de datos
    print('...conexión desde:', addr)  # Imprime la dirección del cliente

    while True:  # Bucle para enviar y recibir datos
        data = client_sock.recv(BUFSIZ)  # Recibe los datos del cliente
        if not data or data.decode('utf-8') == 'END':  # Si no hay datos o se recibe 'END',
            break
        print('Recibido:', data.decode('utf-8'))
        print('Enviando hora del servidor al cliente... {}'.format(ctime()))
        try:
            client_sock.send(ctime().encode('utf-8'))
        except Exception as e:
            print('Error:', e)
        
    client_sock.close()  # Cierra la conexión con el cliente
    print(f'Conexión cerrada con {addr}')

def tcp_server():
    HOST = 'localhost'  # localhost
    PORT = 21567  # puerto de conexión
    ADDR = (HOST, PORT)  # dirección de conexión

    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Crea un socket de conexión
    server_sock.bind(ADDR)  # Asigna la dirección al socket
    server_sock.listen(5)  # Escucha hasta 5 conexiones
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # Reutiliza la dirección

    print('Esperando conexión...')
    while True:
        client_sock, addr = server_sock.accept()  # Acepta la conexión
        print(f'Nueva conexión aceptada de {addr}')
        # Crea un nuevo hilo para manejar la conexión del cliente
        client_thread = threading.Thread(target=handle_client, args=(client_sock, addr))
        client_thread.start()

    server_sock.close()  # Cierra el socket del servidor
        

if __name__ == '__main__':
    tcp_server()

