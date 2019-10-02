from datetime import datetime, timedelta
import random
from base_classes.queue import QueueP2

################################ Class Client #################################


class Client(object):
    def __init__(self, accept_time ):
        self._time_mark = accept_time
        return

    @property
    def time_mark(self):
        return self._time_mark

    def get_wait_time(self, local_time):
        return (local_time - self._time_mark)

####################### Class CashTerminal #################################


class CashTerminal(QueueP2):

    def __init__(self, label):
        super().__init__()
        self._label = label
        return

    @property
    def label(self):
        return self._label

    @property
    def client_count(self):
        return self.count

    def get_max_wait_time(self, current_time):
        ret = timedelta( 0 )
        for client in self.queue:
            if( ret < client.get_wait_time( current_time ) ):
                ret = client.get_wait_time( current_time )
        return ret

    def incoming_client(self, client):
        self.insert_data(client)
        return len(self.queue)

    # Recebe a quantidade de clientes a serem processados e retorna a quantidade efetivamente processada
    def process_clients(self, count):
        ret = 0
        for _ in range(count):
            ret += self.remove_data()
        return ret

    def remove_data(self):
        if(self.count > 0):
            super().remove_data()
            return 1
        return 0

    def get_total_queue_time(self, local_time):
        ret = timedelta(0)
        for client in self.queue:
            ret += client.get_wait_time(local_time)
        return ret

#####################  Class BankAgency #########################


class BankAgency(object):

    def __init__(self, terminal_count, time):
        super().__init__()
        self._terminals = []
        self._local_time = time
        for term_count in range(terminal_count):
            self._terminals.append(CashTerminal(term_count))
        return

    @property
    def local_time(self):
        return self._local_time

    @property
    def client_count(self):
        ret = 0
        for term in self._terminals:
            ret += term.count
        return ret
    
    @property
    def avg_wait_time(self):
        total_time = timedelta(0)
        client_count = 0
        for terminal in self._terminals:
            total_time += terminal.get_total_queue_time(self._local_time)
            client_count += terminal.count
        if(client_count > 0):
            #! validar o resultado
            return total_time.seconds/client_count
        else:
            return 0

    @property
    def max_wait_time(self):
        ret = timedelta(0)
        for term in self._terminals:
            if( ret < term.get_max_wait_time( self._local_time ) ):
                ret = term.max_wait_time
        return ret

    def increment_time(self, delta):
        minutes = timedelta(0, 0, 0, 0, delta)
        self._local_time = self._local_time + minutes
        return self._local_time

    def accept_client(self):
        cash_terminal = self.prior_terminal
        client = Client( self.local_time )
        cash_terminal.incoming_client(client)
        return

    @property
    def prior_terminal(self):
        # Varre lista de caixas para encontrar o com menos clientes
        ret = self._terminals[0]
        for terminal in self._terminals:
            if terminal.client_count < ret.client_count:  # Terminal com menos clientes dentre os existentes
                ret = terminal
        return ret

    def outcoming_clients(self):
        out = 0
        for c in self._terminals:
            # remover clientes entre 1 e 2
            out += c.process_clients(random.randint(1, 2))
        return out

    def incoming_clients(self):
        # Processa as entradas
        incoming_count = random.randint(4, 16)
        for cc in range(incoming_count):
            self.accept_client()
        # Processa as saí­das
        self.outcoming_clients()
        return incoming_count


############### Class SimMediator  ######################

class SimMediator(object):
    def __init__(self, terminal_count):
        super().__init__()
        self._local_time = datetime.now()
        self._agency = BankAgency(terminal_count, self._local_time)
        self._cycle_count = 0
        self._cycle_incoming = 0
        self._cycle_outcoming = 0

    @property
    def cycle_incoming(self):
        return self._cycle_incoming

    @property
    def cycle_outcoming(self):
        return self._cycle_outcoming

    @property
    def cycle_count(self):
        return self._cycle_count

    @property
    def local_time(self):
        return self._local_time

    @property
    def agency(self):
        return self._agency

    def do_cycle(self):
        self._agency.increment_time(1)  # tempo em minutos
        self._cycle_incoming = self._agency.incoming_clients()
        self._cycle_outcoming = self._agency.outcoming_clients()
        return
