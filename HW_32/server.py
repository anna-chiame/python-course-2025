import socket

HOST = "127.0.0.1"
PORT = 65432
BUFFER_SIZE = 1024

# UDP = SOCK_DGRAM
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind((HOST, PORT))
    print(f"UDP server started on {HOST}:{PORT}")

    while True:
        data, client_addr = sock.recvfrom(BUFFER_SIZE)  # (bytes, (ip, port))
        print("Received from", client_addr, ":", data)

        if not data:
            continue


        sock.sendto(data.upper(), client_addr)
