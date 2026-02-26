import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from node import Node

class DoublyNode(Node):
    def __init__(self, item, next=None, prev=None):
        super().__init__(item)
        self.next = next
        self.prev = prev