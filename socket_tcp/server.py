import socket
import sys


ip = '127.0.0.1' # server ip
port = 8080 # server port
addr = (ip, port) # server address


# AF = Address Family
# INET = IPv4
# SOCK_STREAM = TCP, which is a connection-oriented protocol
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    print(f'Starting server at address: {ip}:{port}')

    server.bind(addr)
    server.listen(1)

    while True:
        print('Waiting for someone to connect...')

        conn, client_addr = server.accept()

        client_ip, client_port = client_addr

        print(f'{client_ip} has been connected using port {client_port}')

        with conn:
            while True:
                print('Waiting for messages...')
                msg = conn.recv(1024)

                if msg:
                    print(f'Message from {client_ip}: {msg.decode()}')
                else:
                    break
