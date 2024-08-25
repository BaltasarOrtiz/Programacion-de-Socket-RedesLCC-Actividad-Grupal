import socket
import threading
import time
from time import ctime

HOST = 'localhost'
PORT = 12345

def handle_client(data, addr, server_socket):
    print(f"Conexión recibida de {addr}")
    
    mensaje = data.decode('utf-8')
    if mensaje.startswith('HORA'):
        # Enviar la hora actual
        respuesta = f"Hora actual: {time.strftime('%Y-%m-%d %H:%M:%S')}"
        server_socket.sendto(respuesta.encode(), addr)
    elif mensaje.startswith('OPERACION'):
        # Procesar la operación matemática
        try:
            operacion = mensaje.split(' ', 1)[1]
            resultado = eval(operacion)
            respuesta = f"Resultado de la operación: {resultado}"
        except Exception as e:
            respuesta = f"Error en la operación: {e}"
        
        server_socket.sendto(respuesta.encode(), addr)
    else:
        # Comando no reconocido
        respuesta = "Comando no reconocido"
        server_socket.sendto(respuesta.encode(), addr)

def servidor_udp():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind((HOST, PORT))
    
    print("Servidor en marcha, esperando conexiones...")

    while True:
        data, ADDR = server_socket.recvfrom(1024)
        threading.Thread(target=handle_client, args=(data, ADDR, server_socket)).start()

if __name__ == "__main__":
    servidor_udp()