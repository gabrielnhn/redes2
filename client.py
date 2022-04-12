import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
# PORT = 65432  # The port used by the server cache
PORT = 65010  # The port used by the server cache

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    while(True):
        req = input(">>>")

        # data = b"{req}"
        data = req.encode('UTF-8')

        s.sendall(data)
        data = s.recv(1024)
        data = eval(data)

        print(f"Cache: {data}")