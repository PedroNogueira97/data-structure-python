from node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return []
        return self._inorder(node.left) + [node.key] + self._inorder(node.right)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if node.key == key:
            return True
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, node):
        if node is None:
            return []
        return [node.key] + self._preorder(node.left) + self._preorder(node.right)

    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, node):
        if node is None:
            return []
        return self._postorder(node.left) + self._postorder(node.right) + [node.key]

    def min(self):
        return self._min(self.root)

    def _min(self, node):
        current = node
        while current and current.left is not None:
            current = current.left
        return current.key

    def max(self):
        return self._max(self.root)

    def _max(self, node):
        current = node
        while current and current.right is not None:
            current = current.right
        return current.key

    #Abaixo metodos a serem implementados
    def remove(self, key):
        ...

    def _remove(self, node, key):
        ...


if __name__ == "__main__":
    bst = BinarySearchTree()
    values = [25, 50, 10, 35, 12, 55]
    for value in values:
        bst.insert(value)
    
    print('Inorder: ' + str(bst.inorder()))
    print('Preorder: ' + str(bst.preorder()))
    print('Postorder: ' + str(bst.postorder()))

    print('Min: ' + str(bst.min()))
    print('Max: ' + str(bst.max()))
    print('Search 12: ' + str(bst.search(12)))
    

    