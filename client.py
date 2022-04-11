import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
# PORT = 65432  # The port used by the server cache
PORT = 65000  # The port used by the server cache

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"request")
    data = s.recv(1024)
    data = eval(data)

print(f"Received {data}")
