import socket
import threading

def handle_client(client_socket, server_socket):
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print(f"Intercepted from client: {data.decode('utf-8')}")
        server_socket.sendall(data)
        
        response = server_socket.recv(1024)
        print(f"Intercepted from server: {response.decode('utf-8')}")
        client_socket.sendall(response)

    client_socket.close()
    server_socket.close()

def start_interceptor():
    # Setup for communication with client
    client_listener_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_listener_socket.bind(('127.0.0.1', 65431))
    client_listener_socket.listen()

    print("Interceptor is listening on port 65431...")

    # Setup for communication with server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(('127.0.0.1', 65432))

    client_socket, addr = client_listener_socket.accept()
    print(f"Client connected from {addr}")

    # Start handling the communication
    client_handler = threading.Thread(target=handle_client, args=(client_socket, server_socket))
    client_handler.start()

if __name__ == "__main__":
    start_interceptor()
