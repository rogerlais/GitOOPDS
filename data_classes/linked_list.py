# Classe LinkedList simplesmente encadeada
# Classe SimpleNode



##############  Class SimpleNode  ################
class SimpleNode(object):
    def __init__(self, value):
        super().__init__()
        self.data = value
        self.next = None

##############  Class SimpleLinkedList  ################

class SimpleLinkedList(object):
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None

    #Adiciona ao final da lista(comportamento padrão)
    def add(self, item):
        node = SimpleNode( item )
        if self.tail == None:
            self.head = node
            self.tail = node
        else:
            self.tail = node