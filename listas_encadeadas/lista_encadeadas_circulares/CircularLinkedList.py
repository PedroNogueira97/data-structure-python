import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from LinkedList import LinkedList
from node import Node
from defaultEquals import defaultEquals

class CircularLinkedList(LinkedList):
    def __init__(self, equals=defaultEquals):
        super().__init__(equals)

    def insert_at(self, index, item):
        if 0 <= index <= self.count:
            node = Node(item)
            current = self.head
            if index == 0:
                if self.head is None:
                    self.head = node
                    node.next = self.head
                else:
                    node.next = current
                    current = self.get_element_at(self.size() - 1)
                    self.head = node
                    current.next = self.head
            else:
                previous = self.get_element_at(index - 1)
                node.next = previous.next
                previous.next = node
            self.count += 1
            return True
        return False

    def remove_at(self, index):
        if 0 <= index <= self.count:
            current = self.head
            if index == 0:
                if self.size() == 1:
                    self.head = None
                else:
                    removed = self.head
                    current = self.get_element_at(self.size() - 1)
                    self.head = self.head.next
                    current.next = self.head
                    current = removed
            else:
                previous = self.get_element_at(index - 1)
                current = previous.next
                previous.next = current.next
            self.count -= 1
            return current.item
        return None

    def push(self, item):
        self.insert_at(self.size(), item)

    def return_list(self):
        items = []
        if self.head is not None:
            current = self.head
            for _ in range(self.size()):
                items.append(current.item)
                current = current.next
        return items
            


