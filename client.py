# client.py
import socket
import threading

HOST = 'localhost'
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            print(f"Message from server: {message}")
        except:
            print("Lost connection to the server.")
            client.close()
            break

def send_message(message):
    client.send(message.encode())

# Start a thread to handle incoming messages
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

# Example sending a message
send_message("Player joined the game.")
