from defaultEquals import defaultEquals
from node import Node

class LinkedList:
    def __init__(self, equals = defaultEquals):
        self.head = None
        self.count = 0
        self.equals = equals

    def get_element_at(self, index):
        if (index >= 0 and index < self.count):
            current = self.head
            i = 0
            while (i < index and current is not None):
                current = current.next
                i += 1
            return current
        return None

    def push(self, element):
        node = Node(element)
        if (self.head is None):
            self.head = node
        else:
            current = self.head
            while (current.next is not None):
                current = current.next
            current.next = node
        self.count += 1

    def insert_at(self,index,element):
        if (index >= 0 and index < self.count):
            node = Node(element)
            if (index == 0):
                current = self.head
                node.next = current
                self.head = node
            else:
                previous = self.get_element_at(index - 1)
                current = previous.next
                node.next = current
                previous.next = node
            self.count += 1
            return True
        return False

    def remove_at(self, index):
        if (index >= 0 and index <= self.count):
            current = self.head
            if (index == 0):
                self.head = current.next
            else:
                previous = self.get_element_at(index - 1)
                current = previous.next
                previous.next = current.next
            self.count -= 1
            return current.item
        return None

    def index_of(self, element):
        current = self.head
        i = 0
        while (i < self.count and current is not None):
            if(self.equals(element, current.item)):
                return i
            current = current.next
            i += 1
        return -1

    def remove(self, element):
        index = self.index_of(element)
        return self.remove_at(index)

    def size(self):
        return self.count

    def is_empty(self):
        return self.size() == 0

    def getHead(self):
        return self.head

    def return_list(self):
        current = self.head
        list = []
        while (current is not None):
            list.append(current.item)
            current = current.next
        return list

    

    

    
            




