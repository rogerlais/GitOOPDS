class BinaryTree(object):
    def __init__( self, value, right = None, left = None ):
        """Recebe valor, nó direito e esquerdo"""
        self.data = value
        self.right = right
        self.left = left
        return

    def findRecursive( self, value ):
        """Acha recursivamente um valor, retornando o nó"""
        if( value == self.data ):
            return self
        else:
            if( self.data > value ):
                return self.left.findRecursive( value )
            else:
                return self.right.findRecursive( value )
    
    def insert( self, value ):
        """Insere valor filho ao nó"""
        if self.data < value:
            if self.right is not None:
                return self.right.insert( value )
            else:
                self.right = BinaryTree( value )
                return self.right
        else:
            if self.left is not None:
                return self.left.insert( value )
            else:
                self.left = BinaryTree( value )
                return self.left

    def findLinear( self, value ):
        """Busca linear por valor"""
        current = self
        while( current is not None):
            if current.data == value:
                return current
            elif current.data < value :
                current = current.left
            else:
                current = current.right

    def __str__(self):
        REROEROREOEROERRRROOOO
        return "(" + str(self.data ) + ", " + self.left + "," + self.right + ")"