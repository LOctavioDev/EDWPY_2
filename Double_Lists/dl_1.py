# LISTAS DOBLEMENETE LIGADAs

class Nodo:
    def __init__(self, data):
        self.data = data
        self.after = None
        self.before = None

class DoublyLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
    
    def empty(self):
        return self.first is None

    def add_end(self, data):
        new_node = Nodo(data)
        if self.empty():
            self.first = self.last = new_node
        else:
            new_node.before = self.last
            self.last.after = new_node
            self.last = new_node
        self.size += 1
    
    def add_start(self, data):
        new_node = Nodo(data)
        if self.empty():
            self.first = self.last = new_node
        else:
            new_node.after = self.first
            self.first.before = new_node
            self.first = new_node
        self.size += 1


doubly_linked_list = DoublyLinkedList()

# ADD to end
doubly_linked_list.add_end(1)
doubly_linked_list.add_end(2)
doubly_linked_list.add_end(3)

# Add to start
doubly_linked_list.add_start(0)

# Show List
current_node = doubly_linked_list.first
while current_node:
    print(current_node.data, end=" ")
    current_node = current_node.after
