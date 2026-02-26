import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from LinkedList import LinkedList
from DoublyNode import DoublyNode
from defaultEquals import defaultEquals

class DoublyLinkedList(LinkedList):
    def __init__(self, equals=defaultEquals):
        super().__init__(equals)
        self.tail = None
    
    def insert_at(self, index, item):
        if 0 <= index <= self.count:
            node = DoublyNode(item)
            current = self.head
            if index == 0:
                if self.head is None:
                    self.head = node
                    self.tail = node
                else:
                    node.next = self.head
                    current.prev = node
                    self.head = node
            elif index == self.count: # Last item
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

    def remove_at(self, index):
        if 0 <= index < self.count:
            current = self.head
            if index == 0:
                self.head = current.next
                # If there's only one item, we update the tail too
                if self.count == 1:
                    self.tail = None
                else:
                    self.head.prev = None
            elif index == self.count - 1: # Last item
                current = self.tail
                self.tail = current.prev
                self.tail.next = None
            else:
                current = self.get_element_at(index)
                previous = current.prev
                # Link previous with next
                previous.next = current.next
                current.next.prev = previous
            self.count -= 1
            return current.item
        return None
                
            

    

    

