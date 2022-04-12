import random
import socket
import os

HOST = "127.0.0.1"
PORTS = [64000, 64001, 64002]

def get_temperature(weather):
    if weather == "hot":
        return random.randint(25, 35)
    else:
        return random.randint(-5, 10)

if __name__ == "__main__":
    retval = os.fork() # Get First + Second

    if retval != 0:
        retval = os.fork() # Get Third

        if retval != 0: # First
            PORT = PORTS[0]
        else: # Third
            PORT = PORTS[2]

    else: # Second
        PORT = PORTS[1]

    if random.randint(0, 1):
        weather = "hot"
    else:
        weather = "cold"


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
                conn.sendall(str(get_temperature(weather)).encode("utf-8"))
