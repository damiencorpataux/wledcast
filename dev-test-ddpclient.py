import socket
import time

# Simulate sending a discovery request
client_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_sock.sendto(b'DDP discovery', ('127.0.0.1', 4048))
response, _ = client_sock.recvfrom(1024)
print('Received discovery response:', response)

# Simulate sending DDP data
pixel_data = bytes([255, 0, 0] * 2289)  # red pixels
ddp_packet = b'DDP' + bytes(7) + pixel_data
while True:
    print(f'Sendinf DDP {len(ddp_packet)}')
    client_sock.sendto(ddp_packet, ('127.0.0.1', 4048))
    time.sleep(.1)