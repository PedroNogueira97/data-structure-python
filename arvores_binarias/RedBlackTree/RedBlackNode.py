from Node import Node

class RedBlackNode(Node):
    def __init__(self, key):
        super().__init__(key)
        self.key = key
        self.color = Colors.RED
        self.parent = None

    def is_red(self):
        return self.color == Colors.RED

