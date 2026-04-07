class RedBlackTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = RedBlackNode(key)
            self.root.color = Colors.BLACK
        else:
            newNode = self._insert(self.root, key)
            self.fixTreeProperties(newNode)

    def _insert(self, node, key):
        ...

    def fixTreeProperties(self, node):
        ...