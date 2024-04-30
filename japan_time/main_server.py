import socket
import time




class Server:

    def wait():
        time.sleep(0.00000000001)


    def __init__(self, host='127.0.0.1', port=65432):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen()
        self.client_socket = None
        print(f"Server started, listening on {host}:{port}")

    def accept_connection(self):
        self.client_socket, addr = self.server_socket.accept()
        print(f"Connected to {addr}")

    def send_message(self, message):
        if self.client_socket:
            try:
                self.client_socket.sendall(message.encode('utf-8'))
                if message == '!CLOSE':
                    print("Shutting down server.")
                    self.client_socket.close()
            except Exception as e:
                print(f"Error sending message: {e}")

    def close_server(self):
        if self.client_socket:
            self.client_socket.close()
        self.server_socket.close()
        print("Server shutdown successfully.")

if __name__ == '__main__':
    server = Server()
    try:
        server.accept_connection()
        server.send_message("connected to host")
    except KeyboardInterrupt:
        server.close_server()


