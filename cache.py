import socket

HOST = "127.0.0.1"  # (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

values = [30, 10, 15]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Internet, TCP

    s.bind((HOST, PORT))
    
    # Wait for client
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(str(values).encode("utf-8"))
