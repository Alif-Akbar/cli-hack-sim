class BST:
    def __init__(self):
        pass
    
    def preorder(self, node):
        if node is not None:
            print(node.data, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)
    
    def inorder(self, node):
        self.in_order(node.left)
        print(node.data, end=' ')
        self.in_order(node.right)
    
    def postorder(self, node):
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.data, end=' ')