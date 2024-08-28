import socket

def tcp_client():
    HOST = input("Ingrese la direccion del host: ")
    PORT = int(input("Ingrese el puerto: ")) 
    ADDR = (HOST, PORT)
    BUFSIZ = 1024

    try:
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(ADDR)
        client_sock.send("Hola soy el cliente: {}".format(client_sock.getsockname()).encode('utf-8'))
        print(client_sock.recv(BUFSIZ).decode('utf-8'))

        while True:
            print(client_sock.recv(BUFSIZ).decode('utf-8')) 
            opcion = input("Ingrese una opcion: ")
            client_sock.send(opcion.encode('utf-8')) 

            if opcion == '1':
                operacion = input("Ingrese la operacion: ")
                client_sock.send(operacion.encode('utf-8'))
                print(client_sock.recv(BUFSIZ).decode('utf-8')) 
            elif opcion == '2':
                print(client_sock.recv(BUFSIZ).decode('utf-8'))
            elif opcion == '3':
                print('Conexión cerrada')
                break
    except Exception as e:
        print('Error:', e)
        return


if __name__ == '__main__':
    tcp_client()