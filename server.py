# server.py
import socket
import threading

HOST = 'localhost'
PORT = 5000

# Create and set up server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()
print("Server started, waiting for connections...")

clients = []

def handle_client(client):
    while True:
        try:
            message = client.recv(1024).decode()
            if message:
                print(f"Received: {message}")
                broadcast(message, client)
        except:
            clients.remove(client)
            client.close()
            break

def broadcast(message, sender):
    for client in clients:
        if client != sender:
            client.send(message.encode())

def start_server():
    while True:
        client, _ = server.accept()
        clients.append(client)
        print("New client connected.")
        threading.Thread(target=handle_client, args=(client,)).start()

if __name__ == "__main__":
    start_server()
