import socket
import pickle
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37020))

time.sleep(10)

while True:
    data, addr = client.recvfrom(1024)
    print("To aqui")
    data = pickle.loads(data)
    print("received message: {} from {}".format(data, addr[0]))

data, addr = client.recvfrom(1024)
data = pickle.loads(data)
print("received message: {} from {}".format(data, addr[0]))