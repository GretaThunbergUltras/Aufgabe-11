import socket

receiverIP = "192.168.43.83"
receiverPort = 32127
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.sendto((49).to_bytes(2, byteorder = "little"), (receiverIP, receiverPort))