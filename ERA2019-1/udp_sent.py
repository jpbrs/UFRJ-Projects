import socket
import time
import pickle

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Set a timeout so the socket does not block
# indefinitely when trying to receive data.
server.settimeout(2)
server.bind(("", 44444))


message = pickle.dumps("H2")
server.sendto(message, ('<broadcast>', 37020))
print("message sent!")
message = pickle.dumps("I2")
server.sendto(message, ('<broadcast>', 37020))
print("message sent!")