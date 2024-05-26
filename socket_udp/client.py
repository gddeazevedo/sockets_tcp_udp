import socket
import os


server_ip = '127.0.0.1'
server_port = 5000
server_addr = (server_ip, server_port)

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    while True:
        msg = input('Enter your message: ')
        os.execl('clear')

        if msg == 'exit':
            break

        client.sendto(bytes(msg, 'utf8'), server_addr)
