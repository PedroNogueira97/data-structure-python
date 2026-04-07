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
        if key < node.key:
            if node.left is None:
                node.left = RedBlackNode(key)
                node.left.parent = node
                return node.left
            else:
                return self._insert(node.left, key)
        else if node.right is None:
            node.right = RedBlackNode(key)
            node.right.parent = node
            return node.right
        else:
            return self._insert(node.right, key)

    def fixTreeProperties(self, node):
        while node and node.parent and node.parent.color.is_red() 
        and node.color is not Colors.BLACK:
            parent = node.parent
            grandParent = parent.parent
            #Caso A: o pai é o filho à esquerda
            if grandParent and grandParent.left == parent:
                uncle = grandParent.right
                #Caso 1A: o tio do nó também é vermelho - basta recolorir
                if uncle and uncle.color is Colors.RED:
                    grandParent.color = Colors.RED
                    parent.color = Colors.BLACK
                    uncle.color = Colors.BLACK
                    node = grandParent
                else:
                    #Caso 2A: o nó é o filho à direita - rotação à esquerda
                    #Caso 3A: o nó é o filho à esquerda - rotação à direita
            else: #Caso B: o pai é o filho à direita
                uncle = grandParent.left
                #Caso 1B: o tio é vermelho - basta recolorir
                if uncle and uncle.color is Colors.RED:
                    grandParent.color = Colors.RED
                    parent.color = Colors.BLACK
                    uncle.color = Colors.BLACK
                    node = grandParent
            else:
                #Caso 2B: o nó é o filho à esquerda - rotação à direita
                #Caso 3B: o nó é o filho à direita - rotação à esquerda
        self.root.color = Colors.BLACK

            