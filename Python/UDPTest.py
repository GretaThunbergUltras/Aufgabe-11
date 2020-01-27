import socket

receiverIP = "192.168.43.83"
receiverPort = 32127
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.sendto("Hello Worldx\0", (receiverIP, receiverPort))