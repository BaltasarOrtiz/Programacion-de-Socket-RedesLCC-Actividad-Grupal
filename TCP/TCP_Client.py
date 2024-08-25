import socket

def tcp_client():
    HOST = input("Ingrese la direccion del host: ")
    PORT = int(input("Ingrese el puerto: ")) 
    ADDR = (HOST, PORT)
    BUFSIZ = 4096 # MTU de la red, tamaño de los paquetes de datos que se envian por la red

    try:
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #crea un socket de conexion
        client_sock.connect(ADDR) #se conecta al servidor
        client_sock.send("Hola soy el cliente: {}".format(client_sock.getsockname()).encode('utf-8')) #envia un mensaje al servidor
        print(client_sock.recv(BUFSIZ).decode('utf-8')) #recibe un mensaje del servidor

        while True:
            print(client_sock.recv(BUFSIZ).decode('utf-8')) #recibe un mensaje del servidor
            opcion = input("Ingrese una opcion: ")
            client_sock.send(opcion.encode('utf-8')) #envia un mensaje al servidor

            if opcion == '1':
                operacion = input("Ingrese la operacion: ")
                client_sock.send(operacion.encode('utf-8')) #envia un mensaje al servidor
                print(client_sock.recv(BUFSIZ).decode('utf-8')) #recibe un mensaje del servidor
            elif opcion == '2':
                print(client_sock.recv(BUFSIZ).decode('utf-8')) #recibe un mensaje del servidor
            elif opcion == '3':
                print('Conexión cerrada')
                break

    except Exception as e:
        print('Error:', e)
        return


if __name__ == '__main__':
    tcp_client()