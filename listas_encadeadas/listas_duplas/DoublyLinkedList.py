from LinkedList import LinkedList
from DoublyNode import DoublyNode
from defaultEquals import defaultEquals

class DoublyLinkedList(LinkedList):
    def __init__(self, equals = defaultEquals):
        super().__init__(equals)
        self.tail = None
    
    def insert_at(self, element, index):
        if (index >= 0 and index <= self.count):
            node = DoublyNode(element)
            current = self.head
            if (index == 0):
                if (self.head == None):
                    self.head = node
                    self.tail = node
                else:
                    node.next = self.head
                    current.prev = node
                    self.head = node
            elif (index == self.count): #Ultimo item
                current = self.tail
                current.next = node
                node.prev = current
                self.tail = node
            else:
                previous = self.get_element_at(index - 1)
                current = previous.next
                node.next = current
                previous.next = node
                current.prev = node
                node.prev = previous
            self.count += 1
            return True
        return False
            

    

    

