import socket

target_host = '127.0.0.1'
target_port = 9997

#создаем сокет для работы с UDP
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#отправляем информацию
client.sendto(b"AAABBBCCC", (target_host, target_port))

#получаем информацию
data, addr = client.recvfrom(4096)

print(data.decode())
client.close()