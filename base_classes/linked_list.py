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
        self.head = None
        return

    @property
    def last(self):
        """Retorna o último no da lista"""
        ret = self.head
        while ret != None:
            ret = ret.next
        return ret

    @property
    def count(self):
        """Total de nos na lista"""
        ret = 0
        current = self.head
        while current != None:
                ret += 1
                current = current.next
        return ret

    def __str__(self):
        """Converte lista para cadeia de caracteres"""
        ret = ''
        format_str = '%s' + str(len(str(self.count)))
        current = self.head
        index = 0
        while current != None:
            index += 1
            ret += format(index, format_str) + ': ' + current.value
        return ret

    def add_value(self, value):
        """Adiciona ao final da lista(comportamento padrão).
        Recebe o dado a ser inserido e cria no a partir dele"""
        node = SimpleNode(value)
        return self.add_node(node)

    def add_node(self, node):
        """Adiciona ao final da lista(comportamento padrão).
        Recebe o Node a ser inserido e cria no a partir dele"""
        if self.head == None:
            self.head = node
        else:
            l = self.last
            if l != None:
                l.next = node
            else:
                self.head = node
        return node

    def remove_first(self):
        """Remove o primeiro node e o retorna"""
        rem = self.head
        if rem != None:
            new_head = self.head.next
        else:
            new_head = None
        self.head = new_head
        return rem

    def find_first_value( self, value ):
        """Retorna a primeira ocorrência do valor na lista na forma de node"""
        current = self.head
        ret = None
        while ret == None:
            if current.value == value:
                ret = current
            else:
                current = current.next
        return ret

class CirculeLinkedList(object):

    def __init__(self):
        self.head = None
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
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self._size += 1
        return new_node

    def insert_tail_value( self, value ):
        new_node = SimpleNode( value )
        return self.insert_tail_node( new_node )

    def insert_tail_node( self, new_node ):
        if self._size == 0 :
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail = new_node
            self.tail.next = self.head
        self._size += 1
        return new_node

    '''! criar metodos
    iterator
    remove_value
    insert_orderded_value
    '''