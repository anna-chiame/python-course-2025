import socket

HOST = "127.0.0.1"
PORT = 65432
BUFFER_SIZE = 4096


def caesar_cipher(text: str, key: int) -> str:
    """
    Encrypts text using the Caesar cipher with the given key.
    Only alphabetic characters are shifted.
    """
    shift = key % 26
    result = []

    for ch in text:
        if "a" <= ch <= "z":
            base = ord("a")
            result.append(chr(base + (ord(ch) - base + shift) % 26))
        elif "A" <= ch <= "Z":
            base = ord("A")
            result.append(chr(base + (ord(ch) - base + shift) % 26))
        else:
            # Non-alphabetic characters are not changed
            result.append(ch)

    return "".join(result)


def parse_message(message: str) -> tuple[int, str]:
    """
    Parses client message in format:
    key=<integer>;msg=<text>
    """
    parts = message.split(";", 1)
    if len(parts) != 2:
        raise ValueError("Invalid format. Use key=<int>;msg=<text>")

    key_part, msg_part = parts

    if not key_part.startswith("key="):
        raise ValueError("Missing key")
    if not msg_part.startswith("msg="):
        raise ValueError("Missing message")

    key = int(key_part[4:])
    text = msg_part[4:]

    return key, text


# Create a UDP socket
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    # Bind the socket to address and port
    sock.bind((HOST, PORT))
    print(f"UDP Caesar server started on {HOST}:{PORT}")

    while True:
        # Receive data and client address
        data, client_address = sock.recvfrom(BUFFER_SIZE)

        print("RAW DATA:", data)
        message = data.decode("utf-8", errors="replace")
        print("DECODED:", repr(message))

        try:
            key, text = parse_message(message)
            print("PARSED KEY:", key)
            print("PARSED TEXT:", repr(text))

            encrypted_text = caesar_cipher(text, key)
            response = encrypted_text
            print("ENCRYPTED:", repr(response))

        except Exception as error:
            response = f"ERROR: {error}"
            print("PARSING/ENCRYPT ERROR:", response)

        sock.sendto(response.encode("utf-8"), client_address)
        print("SENT TO:", client_address)
        print("-" * 40)