from node import Node

class DoublyNode(Node):
    def __init__(self, element, next, prev):
        super().__init__(element, next)
        self.prev = prev