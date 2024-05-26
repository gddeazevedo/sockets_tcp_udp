import socket


ip = '127.0.0.1'
port = 5000
addr = (ip, port)

# AF_INET: Address Family - Internet IPv4
# SOCK_DGRAM: UDP socket, not connection oriented, uses datagrams
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
    print(f'Starting server at address: {ip}:{port}')
    server.bind(addr)

    while True:
        print('Waiting for messages...')
        msg, client_addr = server.recvfrom(1024)

        client_ip, client_port = client_addr

        print(f'{client_ip} has been connected using port {client_port}')
        print(f'Message from {client_ip}: {msg.decode()}')
