
class Node():

    def __init__(self, number):
        self.number = number
        self.orientation = 0  # 0 if the resource is not available and 1 if the resource is available
        self.buffer = []  # array of arrays on format [node,orientation]


    def search_node(self, node):
        for i in self.buffer:
            if i[0] == node:
                return True, i
        return False, i

    def add_buffer(self, node, orientation):
        self.buffer.append([node, orientation])

Node1 = Node(1)
Node1.add_buffer(2,0)
Node1.add_buffer(3,1)

node = Node1.search_node(2)[1][0]
buffer = Node1.buffer

print(buffer)

for i in range(0, len(buffer)):
    if buffer[i][0] == node:
        del(buffer[i])  # Delete the node and append it as the last object in the buffer will help us to reduce the search time of "for"
        buffer.append([node,1])  # because with this logic, if everything works perfectly, the inversor node will always be on the first position of the buffer
        break
    else:
        pass

print(buffer)