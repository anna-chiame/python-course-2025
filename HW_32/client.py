import socket

HOST = "127.0.0.1"
PORT = 65432
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:

    s.connect((HOST, PORT))

    s.send(b"Hello, world")
    data = s.recv(BUFFER_SIZE)

print("Received", repr(data))
