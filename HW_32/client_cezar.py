import socket

HOST = "127.0.0.1"
PORT = 65432
BUFFER_SIZE = 4096
TIMEOUT = 2.0

# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    # Set timeout to avoid infinite blocking
    sock.settimeout(TIMEOUT)

    # Read key and message from user
    key = input("Enter Caesar cipher key (integer): ")
    message = input("Enter message: ")

    # Prepare message for server
    payload = f"key={key};msg={message}"

    # Send data to server
    sock.sendto(payload.encode("utf-8"), (HOST, PORT))

    try:
        # Receive encrypted response
        data, server_address = sock.recvfrom(BUFFER_SIZE)
        print("Received from server:", data.decode("utf-8"))

    except socket.timeout:
        print("No response from server (timeout)")
