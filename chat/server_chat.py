import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("0.0.0.0", 8889))
server.listen(5)

while True:
    sock, addr = server.accept()
    data = sock.recv(4096)
    print(f"Client connected from {addr[0]}, {addr[1]}")
    print(data.decode("utf-8") + "\n")
    sock.send(b"Hello, user!")
    if data == "exit":
        server.close()