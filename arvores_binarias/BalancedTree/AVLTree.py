from binary_search_tree import BinarySearchTree
from BalanceFactor import BalanceFactor

class AVLTree(BinarySearchTree):
    def __init__(self):
        super().__init__()
        self.root = None

    #Método para calcular a altura de um nó, formula: 1 + max(altura(esquerda), altura(direita))
    def get_node_height(self, node):
        if node is None:
            return -1
        return 1 + max(self.get_node_height(node.left), self.get_node_height(node.right))

    #Método para calcular o fator de balanceamento de um nó, formula: altura(esquerda) - altura(direita)
    def get_balance_factor(self, node):
        height_difference = self.get_node_height(node.left) - self.get_node_height(node.right)
        b_factor = BalanceFactor()
        mapping = {
            -2: b_factor.UNBALANCED_RIGHT,
            -1: b_factor.SLIGHTLY_UNBALANCED_RIGHT,
            0: b_factor.BALANCED,
            1: b_factor.SLIGHTLY_UNBALANCED_LEFT,
            2: b_factor.UNBALANCED_LEFT,
        }
        return mapping.get(height_difference, b_factor.BALANCED)

    #Rotação simples para a direita
    def rotationLL(self, node):
        tmp = node.left
        node.left = tmp.right
        tmp.right = node
        return tmp

    #Rotação simples para a esquerda
    def rotationRR(self, node):
        tmp = node.right
        node.right = tmp.left
        tmp.left = node
        return tmp

    #Rotação dupla para a direita e depois para a esquerda
    def rotationLR(self, node):
        node.left = self.rotationLL(node.left)
        return self.rotationRR(node)

    #Rotação dupla para a esquerda e depois para a direita
    def rotationRL(self, node):
        node.right = self.rotationRR(node.right)
        return self.rotationLL(node)

    
        

    

    