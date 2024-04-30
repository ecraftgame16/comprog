import socket
import sys
import os


def connect_and_receive_messages(host='127.0.0.1', port=65432):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        print("Connected to server. Listening for messages...")
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message == '!CLOSE':
                    # Exiting without printing '!CLOSE'
                    sys.exit()
                if message:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print(message)
                # Removed the check for an empty message leading to a break.
            except Exception as e:
                print(f"Error receiving message: {e}")
                break  # Break on exception to avoid infinite loop in case of an error.

        client_socket.close()
        print("Connection closed.")

if __name__ == '__main__':
    connect_and_receive_messages()