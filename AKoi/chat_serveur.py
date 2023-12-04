import socket
import threading
import time
import Akoi_Crypt as crypt

# Liste pour stocker les connexions des clients
clients = []

def broadcast_message(message, sender_socket):
    sender_address = sender_socket.getpeername()
    timestamp = time.strftime('%H:%M:%S', time.localtime())
    sender_info = f"{sender_address[0]}:{sender_address[1]} - {timestamp}"
    full_message = f"{sender_info}: {message}"

    for client in clients:
        if client != sender_socket:
            try:
                client.send(full_message.encode('utf-8'))
            except:
                # Gérer les erreurs de connexion avec le client
                clients.remove(client)

def handle_client(client_socket):
    clients.append(client_socket)
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print(message)
            broadcast_message(message, client_socket)
        except:
            # Gérer les erreurs de connexion avec le client
            clients.remove(client_socket)
            client_socket.close()

def main():

    host = input("Entrer l'adresse du serveur : ")
    port = int(input("Entrer le port du serveur : "))
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Serveur en écoute sur {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connexion entrante de {client_address[0]}:{client_address[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    main()