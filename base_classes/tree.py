class Node(object):

    @staticmethod
    def is_Identical( rn1, rn2 ):
        if (rn1 == None and rn2 == None) : # Ambos vazios -> ok
            return True
        elif (rn1 != None and rn2 == None) :  #filhos desbalanceados por um lado
            return False
        elif (rn1 == None and rn2 != None) : #filhos desbalanceados por um lado
            return False
        else: # dados iguais em ambos e recursivamente para ambos os lados  
            if (rn1._data == rn2._data and Node.is_Identical(rn1.left, rn2.left) and Node.is_Identical(rn1.right, rn2.right)) : 
                return True
            else: 
                return False

    def __init__(self, value, right=None, left=None):
        """Recebe valor, nó direito e esquerdo"""
        self._data = value
        self.__selected = False
        self.right = right
        self.left = left
        return

    def __str__(self):
        if self.__selected: #Indica no selecionado para exibição especial
            return '*' + str( self._data ) + '*'
        else:
            return str( self._data )

    @property
    def selected( self ):
        return self.__selected

    @selected.setter
    def selected( self, value ):
        self.__selected = value

    @property
    def is_leaf( self ):
        return ( not( self.left) and not( self.right) )

    def preorder(self, lst):
        lst.append(self)
        if self.left:
            self.left.preorder(lst)
        if self.right:
            self.right.preorder(lst)
        return lst

    def traversal_inorder(self):
        if self.left:
            yield from self.left.traversal_inorder()
        yield self
        if self.right:
            yield from self.right.traversal_inorder()
        return


    def display(self): 
        """Exibe arvore de forma grafica em modo texto"""
        lines, _, _, _ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            #*line = '%s' % self._data
            line = '%s' % str( self )
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % str( self )
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % str( self )
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % str(self)
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

    def insert_value(self, value):
        """Insere valor filho ao nó"""
        if self._data == value:
            return False
        elif value < self._data:
            if self.left:
                return self.left.insert_value(value)
            else:
                self.left = Node(value)
                return True
        else:
            if self.right:
                return self.right.insert_value(value)
            else:
                self.right = Node(value)
                return True

    def insert_node( self, node ):
        if self._data == node._data:
            return False
        elif node._data < self._data:
            if self.left:
                return self.left.insert_node(node)
            else:
                self.left = node
                return True
        else:
            if self.right:
                return self.right.insert_node(node)
            else:
                self.right = node
                return True

    def postorder(self, lst):
        if self.left:
            self.left.postorder(lst)
        if self.right:
            self.right.postorder(lst)
        lst.append(self)
        return lst

    def find(self, value):
        if self._data == value:
            return self
        elif value < self._data and self.left:
            return self.left.find(value)
        elif value > self._data and self.right:
            return self.right.find(value)
        return None

    def inorder(self, lst):
        if self.left:
            self.left.inorder(lst)
        lst.append(self)
        if self.right:
            self.right.inorder(lst)
        return lst

    def minValueNode(self, node):
        """Retorna no com minimo valor do ramo"""
        current = node
        while(current.left is not None):  # busca folha mais distante 
            current = current.left
        return current

    def deleteNode(self, base, value ): 
        if base is None: 
            return base  

        if value < base._data: # desloca sub-nos esquerdos  
            base.left = self.deleteNode(base.left, value) 

        elif(value > base._data): # desloca sub-nos direitos
            base.right = self.deleteNode(base.right, value) 

        else: #Testa se a referencia/root será removida
            # Casos sem filhos ou unico filho
            if base.left is None : 
                temp = base.right  
                base = None 
                return temp 

            elif base.right is None : 
                temp = base.left
                base = None
                return temp 

            temp = self.minValueNode(base.right) #Busca pelo sucesso em-ordem

            base._data = temp._data #Transfere para o no base o valor do no que assumira papel

            base.right = self.deleteNode(base.right , temp._data) #remove o no que assumiu a base 
        return base  

class BinaryTree(object):

    def __init__(self):
        self._root = None

    @property
    def root_node(self):
        return self._root

    def findRecursive(self, value):
        """Acha recursivamente um valor, retornando o nó"""
        rn = self.root_node
        if(value == rn._data):
            return self
        else:
            if(rn._data > value):
                return self.left.findRecursive(value)
            else:
                return self.right.findRecursive(value)

    def findLinear(self, value):
        """Busca linear por valor"""
        current = self.root_node
        while(current is not None):
            if current._data == value:
                return current
            elif current._data < value:
                current = current.left
            else:
                current = current.right

    def __str__(self):
        """converte node to string"""
        if self.left:
            l = str(self.left._data)
        else:
            l = ""
        if self.right:
            r = str(self.right._data)
        else:
            r = ''
        return "(" + str(self._data) + ", " + l + ", " + r + ")"

    def traversal_inorder(self):
        if self.left:
            yield from self.left.traversal_inorder()
        yield self
        if self.right:
            yield from self.right.traversal_inorder()
        return

    def traversal_posorder(self):
        if self.left:
            yield from self.left.traversal_posorder()
        if self.right:
            yield from self.right.traversal_posorder()
        yield self
        return

    def traversal_preorder(self):
        yield self
        if self.left:
            yield from self.left.traversal_preorder()
        if self.right:
            yield from self.right.traversal_preorder()
        return

    def levels(self):
        """Conta profundidade máxima para ambos os lados"""
        if self.right:
            r = self.right.levels()
        else:
            r = 0
        if self.left:
            l = self.left.levels()
        else:
            l = 0
        return 1 + max(l, r)

    @property
    def childnodes(self):
        """Quantidade de nos filhos"""
        ret = 0
        if self.left:
            ret += (1 + self.left.childnodes)
        if self.right:
            ret += (1 + self.right.childnodes)
        return ret

    @property
    def leafs(self):
        """Quantidade de folhas"""
        if (self.left is None) and (self.right is None):
            ret = 1
        else:
            ret = 0
            if self.left:
                ret += self.left.leafs
            if self.right:
                ret += self.right.leafs
        return ret

    def find(self, d):
        """Referencia ao no se valor encontrado"""
        if self._root:
            return self._root.find(d)
        else:
            return None

    def preorder(self):
        ret = []
        if self._root:
            return self._root.preorder(ret)
        return ret

    def postorder(self):
        ret = []
        if self._root:
            return self._root.postorder(ret)
        return ret

    def inorder(self):
        ret = []
        if self._root:
            return self._root.inorder(ret)
        return ret

    def insert_value(self, value):
        """Retorna false se valor já existe"""
        if self._root:
            return self._root.insert_value(value)
        else:
            self._root = Node(value)
            return True

    def insert_node(self, node ):
        if self._root:
            return self._root.insert_node(node)
        else:
            self._root = node
            return True


    def remove(self, value):
        rn = self.root_node
        if not rn.is_leaf: #algo alem do raiz presente
            node_to_remove = self.find(value)
            if node_to_remove:
                node_to_remove.deleteNode( rn , value )
                return node_to_remove
        elif (not(rn.left) and not( rn.right ) ) and rn._data == value:
            self._root = None
            return rn

    def is_similar( self, tree ):
        """Testa se esta arvore é similar a outra informada"""
        rn1 = self.root_node
        rn2 = tree.root_node
        return Node.is_Identical( rn1, rn2 )