import socket
import os


server_ip = '127.0.0.1'
server_port = 8080

# AF = Address Family
# INET = IPv4
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    server_addr = (server_ip, server_port)

    client.connect(server_addr)

    while True:
        msg = input('Enter your message: ')
        os.system('clear')

        if msg == 'exit':
            break

        client.sendall(bytes(msg, 'utf8'))
