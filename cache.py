import socket

HOST = "127.0.0.1"  # (localhost)
PORT_TO_LISTEN = 65010
PORTS = [64000, 64001, 64002]


server_sockets = []
for port in PORTS:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, port))
    server_sockets.append(s)

listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_sock.bind((HOST, PORT_TO_LISTEN))

while True:
    # Wait for client
    listen_sock.listen()
    conn, addr = listen_sock.accept()
    print(f"Connected by {addr}")

    while(True):
        data = conn.recv(1024)
        if not data:
            break
        
        data = eval(data)
        print(f"Received request {data}")
        if data in range(len(server_sockets)):
            server_sockets[data].sendall("give it to me".encode("utf-8"))

            response = server_sockets[data].recv(1024)
            temperature = eval(response)
        
            conn.sendall(str(temperature).encode("utf-8"))
