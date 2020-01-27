import socket
import struct

receiverIP = "192.168.43.83"
receiverPort = 32127
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.sendto(struct.pack(">i", 2000364432), (receiverIP, receiverPort))
