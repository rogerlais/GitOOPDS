class BinaryTree(object):
    def __init__(self, value, right=None, left=None):
        """Recebe valor, nó direito e esquerdo"""
        self.data = value
        self.right = right
        self.left = left
        return

    def findRecursive(self, value):
        """Acha recursivamente um valor, retornando o nó"""
        if(value == self.data):
            return self
        else:
            if(self.data > value):
                return self.left.findRecursive(value)
            else:
                return self.right.findRecursive(value)

    def insert(self, value):
        """Insere valor filho ao nó"""
        if self.data < value:
            if self.right is not None:
                return self.right.insert(value)
            else:
                self.right = BinaryTree(value)
                return self.right
        else:
            if self.left is not None:
                return self.left.insert(value)
            else:
                self.left = BinaryTree(value)
                return self.left

    def findLinear(self, value):
        """Busca linear por valor"""
        current = self
        while(current is not None):
            if current.data == value:
                return current
            elif current.data < value:
                current = current.left
            else:
                current = current.right

    def __str__(self):
        """converte node to string"""
        if self.left:
            l = str(self.left.data)
        if self.right:
            r = str( self.right.data )
        return "(" + str(self.data) + ", " + l + ", " + r + ")"

    def traversal_inorder( self ):
        if self.left:
           yield self.left.traversal_inorder()
        yield self
        if self.right:
            self.right.traversal_inorder()
        return

    def traversal_posorder( self ):
        if self.left:
            self.left.traversal_inorder()
        if self.right:
            self.right.traversal_inorder()
        yield self
        return

    def traversal_preorder( self ):
        yield self
        if self.left:
            self.left.traversal_preorder()
        if self.right:
            self.right.traversal_preorder()
        return
