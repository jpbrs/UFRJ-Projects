import network

ssid="<YOUR_SSID"
password="YOUR_PASSWORD"

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect()


import usocket as socket
import pickle
import utime as time
import select
import random

################################################## PUBLISH #####################################################################

from umqtt.simple import MQTTClient

c = MQTTClient("","<MQTT_BROKER_IP>")
c.connect()


def publish_mqtt(node):
    tempo = time.localtime()
    msg = "Ano {} Mes {} Dia {} {}:{}:{} ".format(tempo[0],tempo[1],tempo[2],tempo[3],tempo[4],tempo[5])
    msg = msg + " Publicado por {}".format(node)
    c.publish(b"<MQTT_BROKER_TOPIC", msg)


################################################################################################################################


port_send = 37020
port_listen = 37020

sleeptime = 6
sleeptime_plus2 = sleeptime * 2
timeout_in_seconds = 10

def dormir():
    time.sleep(sleeptime+3)


class Node():

    def __init__(self, number):
        self.number = number
        self.orientation = 0 #0 if the resource is not available and 1 if the resource is available
        self.buffer = [] # array of arrays on format [node,orientation]
        self.msg = [self.number, 1]
        self.watchdog = time.time()



        self.client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.client.bind(("", port_listen))
        self.client.settimeout(timeout_in_seconds)
        self.client.setblocking(False)


    def add_buffer(self, node, orientation):
        if self.search_node(node):
            pass
        else:
            self.buffer.append([node, orientation])

    def check_sink_node(self): #Function for return True if all resources of nodes are aveilable for one node transmit the message
        if len(self.buffer)>0:
            for i in self.buffer:
                if i[1]==0:
                    return False
            return True
        else:
            pass

    def search_node(self, node):
        for i in self.buffer:
            if i[0] == node:
                return True
        return False



    def revert_node(self, node): #Function used in case of receive an reverting message
        for i in self.buffer:
            if i[0]==node:
                self.buffer.remove(i)  # Delete the node and append it as the last object in the buffer will help us to reduce the search time  "for"
                self.buffer.append([node, 1])
                break
            else:
                pass
        self.add_buffer(node, 1) #In case of the reversor node is not on the buffer

    def revert_buffer(self): #Function used in case of transmission of reverting message
        for i in self.buffer:
            i[1]=0


    def check_watchdog(self): #Function to check if a node is unused
        t1 = (len(self.buffer)+1)*sleeptime_plus2
        if(time.time()-self.watchdog)>(t1+sleeptime): #Random number of watch will avoid multiples sink node transmissing reverting message at same time.
            for i in self.buffer:                                       #As time passes, the chances of not having simultaneity in the messages will be greater
                if i[1] == 0:
                    print("Nó a ser removido após estouro de watchdog: {}".format(i))
                    self.buffer.remove(i)

                else:
                    pass
            return True
        else:
            return False


    def update_watchdog(self): #Function to sinalyze that one node is not unused
        self.watchdog = time.time()



    def send_hello(self): #Function to send the first message at the initialization of a node
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mensagem = pickle.dumps("H{}".format(self.number))
        server.sendto(mensagem, ('192.168.0.255', port_send))


        print("Node {} sent Hello".format(self.number))


    def send_ack(self, addr): #Function to respond a Hello message to the source
        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mensagem = pickle.dumps("A{}".format(self.number))
        server.sendto(mensagem, ('192.168.0.255', port_send))


        print("Node {} sent Ack to {}".format(self.number, addr))

    def send_reversor(self): #Function used after check that all resources of the node are available


        publish_mqtt(self.number)

        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        mensagem = pickle.dumps("I{}".format(self.number))
        server.sendto(mensagem, ('192.168.0.255', port_send))

        print("Node {} sent reversor".format(self.number))




    def hello_received(self, addr, msg_payload):
        self.send_ack(addr)
        print(self.buffer)

        if self.search_node(msg_payload):
            self.revert_node(msg_payload)
        else:
            self.add_buffer(int(msg_payload), int(1))

        print("Received Hello from Node {} and payload {}".format(addr, msg_payload))
        print(self.buffer)

    def reversor_received(self, node):

        self.revert_node(node)



    def data_analyser(self, data, addr):
        msg_type = data[0]
        msg_payload = int(data[1])

        addr = addr[0]


        if msg_payload==self.number or msg_type=="A":
            pass
        else:
            if msg_type == "H":
                self.hello_received(addr, msg_payload)

            if msg_type == "I":
                self.reversor_received(msg_payload)



    def initialize_node(self):
        self.send_hello()
        dormir()

        ready = select.select([self.client], [], [], timeout_in_seconds)


        if ready[0]:
            data, addr = self.client.recvfrom(1024)
            msg_type = data[0]
            msg_payload = int(data[1])

            if msg_type == "A":
                self.add_buffer(msg_payload, 0)
            else:
                self.data_analyser(data, addr)
        else:
            pass


    def main(self):



        while True:

            ready = select.select([self.client], [], [], timeout_in_seconds)

            if ready[0]:
                print("Has data")
                data, addr = self.client.recvfrom(1024)
                data = pickle.loads(data)

                if int(data[1]) == self.number:
                    pass

                else:
                    self.data_analyser(data, addr)
                    print("Received message: {} from {}".format(data, addr[0]))
                    print("Buffer: {}".format(self.buffer))

                    if self.check_sink_node() or self.check_watchdog():

                        print(time.time() - self.watchdog)

                        self.send_reversor()
                        self.revert_buffer()
                        if self.check_watchdog():
                            print("Node {} sending reversor because of watchdog".format(self.number))
                        if self.check_sink_node():
                            print("Node {} sending reversor because is the sink node".format(self.number))
                        self.update_watchdog()

                    dormir()



            else:
                print("There is no data")
                if self.check_sink_node() or self.check_watchdog():

                    print(time.time() - self.watchdog)

                    self.send_reversor()
                    self.revert_buffer()
                    if self.check_watchdog():
                        print("Node {} sending reversor because of watchdog".format(self.number))
                    if self.check_sink_node():
                        print("Node {} sending reversor because is the sink node".format(self.number))
                    self.update_watchdog()

                dormir()

def main():
    Node4 = Node(4)
    Node4.initialize_node()
    Node4.main()

if __name__ == "__main__":
    main()