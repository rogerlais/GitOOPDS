from datetime import datetime, timedelta
import random
from base_classes.queue import QueueP2

################################ Class Client #################################


class Client(object):
    def __init__(self):
        self.time_mark = datetime.now()
        return

    def get_time_mark(self):
        return self.time_mark

    def get_wait_time(self, local_time ):
        return ( local_time - self.time_mark )

####################### Class CashTerminal #################################

class CashTerminal(QueueP2):
    
    def __init__(self, label):
        super().__init__()
        self._label = label
        return

    @property
    def label(self):
        return self._label

    def incoming_client(self, client):
        self.insert_data(client)
        return len(self.get_queue())

    #Recebe a quantidade de clientes a serem processados e retorna a quantidade efetivamente processada
    def process_clients(self, count):
        ret = 0
        for _ in range(count):
            ret += self.remove_data()
        return ret

    def remove_data(self):
        if( len( self.data ) > 0 ):
            super().remove_data()
            return 1
        return 0

    def get_client_queue(self):
        return self.get_queue()

    def get_total_queue_time(self, local_time ):
        ret = timedelta(0)
        for c in self.data:
            ret += c.get_wait_time( local_time )
        return ret

    def get_client_count(self):
        return self.get_count()

#####################  Class BankAgency #########################


class BankAgency(object):

    def __init__(self, cash_count, time ):
        # super().__init__(self)
        self.cashes = []
        self.local_time = time
        for c in range(cash_count):
            self.cashes.append(CashTerminal(c))
        return

    def increment_time( self , delta ):
        minutes = timedelta(0,0,0,0,delta)
        self.local_time = self.local_time + minutes
        return self.local_time

    def incoming_client(self):
        cash_terminal = self.get_prior_terminal()
        client = Client()
        cash_terminal.incoming_client(client)
        return

    def get_prior_terminal(self):
        # Varre lista de caixas para encontrar o com menos clientes
        ret = self.cashes[0]
        for terminal in self.cashes:
            if ret.get_client_count() < terminal.get_client_count():
                ret = terminal
        return ret

    def outcoming_clients(self):
        out = 0
        for c in self.cashes:
            # remover clientes entre 1 e 2
            out += c.process_clients(random.randint(1, 2))
        return out

    def incoming_clients(self):
        # Processa as entradas
        incoming_count = random.randint(4, 16)
        for cc in range(incoming_count):
            self.incoming_client()
        # Processa as saídas
        self.outcoming_clients()
        return incoming_count

    def get_avg_wait_time(self):
        total_time = timedelta(0)
        client_count = 0
        for c in self.cashes:
            total_time += c.get_total_queue_time( self.local_time )
            client_count += c.get_client_count()
        if( client_count > 0 ):
            #! validar o resultado
            return total_time/client_count
        else:
            return 0
