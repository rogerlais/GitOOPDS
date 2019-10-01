# Classe LinkedList simplesmente encadeada
# Classe SimpleNode



##############  Class SimpleNode  ################
class SimpleNode(object):
    def __init__(self, value):
        super().__init__()
        self.data = value
        self.next = None

    def insert_next( self, value ):
        next_value = SimpleNode( value )
        self.next = next_value

##############  Class SimpleLinkedList  ################

class SimpleLinkedList(object):

    #constructor
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        return

    #Adiciona ao final da lista(comportamento padrão)
    def add(self, item):
        node = SimpleNode( item )
        if self.tail == None:
            self.head = node
            self.tail = node
        else:
            self.tail = node
        return node

    #Total de nos na lista
    def get_count( self ):
        ret = 0
        current = self.head
        while current != None:
            ret += 1
            current = current.next
        return ret

    def remove_first(self):
        rem = self.head
        if rem != None:
            new_head = self.head.next
        

