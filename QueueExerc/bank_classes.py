from datetime import datetime
import random
import queueP2

################################ Client #################################
class Client(object):
    def __init__(self):
        self.timestamp = datetime.timestamp()
        return

    def get_timestamp( self ):
        return self.timestamp

####################### CashTerminal #################################

class CashTerminal(queueP2.QueueP2):
    def __init__(self):
        
        #self.client_list = queueP2.QueueP2()
        return

    def incoming_client( self, client ):
        self.insert_data( client )
        return len( self.get_queue() )

    def process_clients( self, count ):
        for _ in range( count ):
            self.remove_data()
        return len( self.get_queue)

    def get_client_queue(self):
        return self.get_queue()

#####################  BankAgency #########################
class BankAgency(object):
    
    def __init__(self, cash_count):
        super().__init__(self)
        self.cashes = []
        for _ in range( cash_count):
            self.cashes.append( CashTerminal() )
        return

    def incoming_client( self ):
        cash_terminal = self.get_prior_terminal()
        client = Client()
        cash_terminal.incoming_client( client )
        return

    def get_prior_terminal(self):
        #Varre lista de caixas para encontrar o com menos clientes
        ret = self.cashes[0]
        for terminal in self.cashes:
            if ret.get_client_count() < terminal.get_client_count():
                ret = terminal
        return ret

    def outcoming_clients( self ):
        out = 0
        for c in self.cashes:
            #remover clientes entre 1 e 2
            out += c.process_clients( random.randint( 1,2 ))
        return out

    def incoming_clients( self ):
        #Processa as entradas
        incoming_count = random.randint(4, 16)
        for cc in range( incoming_count):
            self.incoming_client()
        #Processa as saídas
        self.outcoming_clients()
        return incoming_count

    def get_avg_wait_time(self):
        total_time = 0
        client_count = 0
        for c in self.cashes:
            clientlist = c.get_client_queue()
            for item in range( len( clientlist )):
                clientlist += 1
                total_time += item.get_wait_time()
        return total_time/client_count