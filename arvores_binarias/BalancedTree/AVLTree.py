from binary_search_tree import BinarySearchTree
from BalanceFactor import BalanceFactor

class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()
        self.root = None

    #Método para calcular a altura de um nó, formula: 1 + max(altura(esquerda), altura(direita))
    def get_node_height(self, node):
        return node.height if node is not None else -1

    #Método para calcular o fator de balanceamento de um nó, formula: altura(esquerda) - altura(direita)
    def get_balance_factor(self, node):
        height_difference = self.get_node_height(node.left) - self.get_node_height(node.right)
        if height_difference > 1:
            return BalanceFactor.UNBALANCED_LEFT
        elif height_difference < -1:
            return BalanceFactor.UNBALANCED_RIGHT
        return BalanceFactor.BALANCED

    #Rotação simples para a direita
    def rotationLL(self, node):
        tmp = node.left
        node.left = tmp.right
        tmp.right = node
        node.height = 1 + max(self.get_node_height(node.left), self.get_node_height(node.right))
        tmp.height = 1 + max(self.get_node_height(tmp.left), self.get_node_height(tmp.right))
        return tmp

    #Rotação simples para a esquerda
    def rotationRR(self, node):
        tmp = node.right
        node.right = tmp.left
        tmp.left = node
        node.height = 1 + max(self.get_node_height(node.left), self.get_node_height(node.right))
        tmp.height = 1 + max(self.get_node_height(tmp.left), self.get_node_height(tmp.right))
        return tmp

    #Rotação dupla para a direita e depois para a esquerda
    def rotationLR(self, node):
        node.left = self.rotationLL(node.left)
        return self.rotationRR(node)

    #Rotação dupla para a esquerda e depois para a direita
    def rotationRL(self, node):
        node.right = self.rotationRR(node.right)
        return self.rotationLL(node)

    #Método para inserir um nó na árvore
    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        else:
            return node
        node.height = 1 + max(
            self.get_node_height(node.left), 
            self.get_node_height(node.right)
        )

        #Balancear a árvore, se necessário
        balance_f = self.get_balance_factor(node)
        #Caso 1: Árvore desbalanceada para a esquerda
        if balance_f == BalanceFactor.UNBALANCED_LEFT:
            if key < node.left.key:
                return self.rotationLL(node)
            else:
                return self.rotationLR(node)
        #Caso 2: Árvore desbalanceada para a direita
        if balance_f == BalanceFactor.UNBALANCED_RIGHT:
            if key > node.right.key:
                return self.rotationRR(node)
            else:
                return self.rotationRL(node)
        return node
    
        

    

    