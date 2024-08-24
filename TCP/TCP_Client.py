import socket
import sys

def tcp_client():
    HOST = input("Ingrese la direccion del HOST: ") #pide la direccion IP del servidor
    PORT = int(input("Ingrese el puerto: ")) #pide el puerto del servidor
    ADDR = (HOST, PORT) #direccion del servidor
    BUFSIZ = 4096 # MTU de la red, tamaño de los paquetes de datos que se envian por la red

    client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #crea un socket de conexion
    client_sock.connect(ADDR) #se conecta al servidor

    while True: #bucle para enviar y recibir datos
        data = f'GET / HTTP/1.1\r\n\n\nHost: {HOST}' #datos a enviar
        if not data: # si no hay datos,
            break # sale del bucle
        client_sock.send(data.encode('utf-8')) #envia los datos al servidor
        data = client_sock.recv(BUFSIZ) #recibe los datos del servidor
        if not data: #si no hay datos,
            break #sale del bucle
            
        print(data.decode('utf-8')) #imprime los datos recibidos

    client_sock.close() #cierra la conexion


if __name__ == '__main__':
    tcp_client()