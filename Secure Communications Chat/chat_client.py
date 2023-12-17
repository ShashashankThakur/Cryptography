import socket
import ssl
import threading

def receive_messages(ssl_socket):
    """
    Receive and print messages in a separate thread.

    :param ssl_socket: The SSL socket.
    """
    while True:
        message = ssl_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Received message: {message}")

def start_client():
    """
    Start the chat client.
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ssl_client = ssl.wrap_socket(client_socket, keyfile=None, certfile=None, server_side=False, ssl_version=ssl.PROTOCOL_TLS)

    ssl_client.connect(('localhost', 9999))
    print("Connected to the chat server.")

    receive_thread = threading.Thread(target=receive_messages, args=(ssl_client,))
    receive_thread.start()

    while True:
        message = input("Your message: ")
        ssl_client.send(message.encode('utf-8'))

if __name__ == "__main__":
    start_client()
