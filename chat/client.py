import socket

target_host = "127.0.0.1"
target_port = 8889


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

nickename = input("Please, enter your nickname: ").lstrip().rstrip()

client.connect((target_host, target_port))

while True:
    
    message = (nickename + " " + input("Enter, your message: ").lstrip().rstrip())

    client.send(message.encode())

    answer = client.recv(4096)

    print(answer.decode("utf-8"))