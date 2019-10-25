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
        else:
            l = ""
        if self.right:
            r = str( self.right.data )
        else:
            r = ''
        return "(" + str(self.data) + ", " + l + ", " + r + ")"

    def traversal_inorder( self ):
        if self.left:
           yield from self.left.traversal_inorder()
        yield self
        if self.right:
            yield from self.right.traversal_inorder()
        return

    def traversal_posorder( self ):
        if self.left:
            yield from self.left.traversal_posorder()
        if self.right:
            yield from self.right.traversal_posorder()
        yield self
        return

    def traversal_preorder( self ):
        yield self
        if self.left:
            yield from self.left.traversal_preorder()
        if self.right:
            yield from self.right.traversal_preorder()
        return

    def levels(self):
        """Conta profundidade máxima para ambos os lados"""
        if self.right :
            r = self.right.levels()
        else:
            r = 0
        if self.left:
            l = self.left.levels()
        else:
            l = 0
        return 1 + max( l, r )

    @property
    def childnodes(self):
        """Quantidade de nos filhos"""
        ret = 0
        if self.left:
            ret += ( 1 + self.left.childnodes)
        if self.right:
            ret += ( 1 + self.right.childnodes)
        return ret

    @property
    def leafs(self):
        """Quantidade de folhas"""
        if ( self.left is None) and ( self.right is None):
            ret =  1
        else:
            ret = 0
            if self.left:
                ret += self.left.leafs
            if self.right:
                ret += self.right.leafs
        return ret

    def toPlainText(self, cols ):
        """Gera texto para apresentação da árvore"""
        line = str( self.data ) .center( cols )
        if self.left:
            linkLine = ('/' + '-'*(5)).center( cols // 2 )
        ret =  line + "\n" + linkLine
        return ret