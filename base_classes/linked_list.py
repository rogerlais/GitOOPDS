# Classe LinkedList simplesmente encadeada
# Classe SimpleNode


##############  Class SimpleNode  ################
class SimpleNode(object):
    """Classe de Nó para lista simplemente encadeada"""

    def __init__(self, value):
        """Instancia Nó para estrutura de lista simple. Recebe o seu valor"""
        super().__init__()
        self.data = value
        self.next = None

    @property
    def value(self):
        """Valor associado ao node"""
        return self.data

    def insert_next(self, value):
        """Insere novo nó a seguir desta instância na lista"""
        next_value = SimpleNode(value)
        if self.next != None:
            next_value.next = self.next
        self.next = next_value

##############  Class SimpleLinkedList  ################

class SimpleLinkedList(object):
    """Abstração para lista simplemente encadeada"""

    def __init__(self):
        """Instancia lista simplemente encadeada"""
        super().__init__()
        self.__head = None
        return

    @property
    def last(self):
        """Retorna o último no da lista"""
        ret = self.__head
        if ret != None:
            if ret.next != None:
                ret = ret.next
                while ret.next != None:
                    ret = ret.next
        return ret

    @property
    def count(self):
        """Total de nos na lista"""
        ret = 0
        current = self.__head
        while current != None:
                ret += 1
                current = current.next
        return ret

    @property
    def head(self):
        return self.__head

    def __str__(self):
        """Converte lista para cadeia de caracteres"""
        ret = ''
        format_str = "{0:d} : {1:s} \r\n"
        current = self.__head
        index = 0
        while current != None:
            index += 1
            ret += format_str.format( index, str(current.value) )
            current = current.next
        return ret

    def add_value(self, value):
        """Adiciona ao final da lista(comportamento padrão).
        Recebe o dado a ser inserido e cria no a partir dele"""
        node = SimpleNode(value)
        return self.add_node(node)

    def add_node(self, node):
        """Adiciona ao final da lista(comportamento padrão).
        Recebe o Node a ser inserido e cria no a partir dele"""
        if self.__head == None:
            self.__head = node
        else:
            lst = self.last #Atualiza referencia do proximo para o demovido ultimo 
            if lst != None:
                lst.next = node
        return node

    def remove_first(self):
        """Remove o primeiro node e o retorna"""
        rem = self.__head
        if rem != None:
            new_head = self.__head.next
        else:
            new_head = None
        self.__head = new_head
        return rem

    def find_first_value( self, value ):
        """Retorna a primeira ocorrência do valor na lista na forma de node"""
        current = self.__head
        ret = None
        while ret == None:
            if current.value == value:
                ret = current
            else:
                current = current.next
        return ret

class CirculeLinkedList(object):

    def __init__(self):
        self.__head = None
        self.tail = None
        self._size = 0
        return

    @property
    def size(self):
        return self._size

    def insert_head_value( self, value ):
        """Insert a node value at head from list"""
        new_node = SimpleNode( value )
        return self.insert_head_node( new_node )

    def insert_head_node( self, new_node ):
        """insert a node at head from list"""
        if self.size == 0 :
            self.__head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.__head
            self.__head = new_node
            self.tail.next = self.__head
        self._size += 1
        return new_node

    def insert_tail_value( self, value ):
        new_node = SimpleNode( value )
        return self.insert_tail_node( new_node )

    def insert_tail_node( self, new_node ):
        if self._size == 0 :
            self.__head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail = new_node
            self.tail.next = self.__head
        self._size += 1
        return new_node

    '''! criar metodos
    iterator
    remove_value
    insert_orderded_value
    '''