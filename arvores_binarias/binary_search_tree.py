from node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        elif key < self.root.key:
            if self.root.left is None:
                self.root.left = Node(key)
            else:
                self.insert(self.root.left, key)
        elif self.root.right is None:
            self.root.right = Node(key)
        else:
            self.insert(self.root.right, key)