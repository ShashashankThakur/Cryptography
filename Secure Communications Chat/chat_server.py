import socket
import ssl
import threading

def handle_client(client_socket):
    """
    Handle a single client in a separate thread.

    :param client_socket: The client socket.
    """
    # Wrap the socket with SSL
    ssl_client = ssl.wrap_socket(client_socket, server_side=True, keyfile="server-key.pem", certfile="server-cert.pem", ssl_version=ssl.PROTOCOL_TLS)

    # Receive and send messages
    while True:
        message = ssl_client.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Received message: {message}")

        response = input("Server response: ")
        ssl_client.send(response.encode('utf-8'))

    ssl_client.close()

def start_server():
    """
    Start the chat server.
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 9999))
    server_socket.listen(5)

    print("Chat server listening on port 9999...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
