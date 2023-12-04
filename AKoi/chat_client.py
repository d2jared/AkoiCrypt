import socket
import threading
import time
import Akoi_Crypt as crypt

SEPARATOR = " | "

def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        message = message.split(SEPARATOR)
        cipherText = message[0]
        cle = message[1]
        message = crypt.Decrypt(cipherText, cle)
        print(message)

def main():
    host = input("Entrer l'adresse du serveur : ")
    port = int(input("Entrer le port du serveur : "))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input(time.strftime('%H:%M:%S', time.localtime()) + ' - Vous: ')
        cipherText = crypt.Encrypt(message, crypt.cle)
        sms = cipherText + SEPARATOR + crypt.cle.hex()
        client_socket.send(sms.encode('utf-8'))

if __name__ == '__main__':
    main()