from datetime import datetime, timedelta
import random
from base_classes.queue import QueueP2

################################ Class Client #################################


class Client(object):
    """Classe para abstração de cliente do banco"""

    def __init__(self, accept_time):
        """Construtor recebe a marca de tempo de entrada do cliente"""
        self._time_mark = accept_time
        return

    @property
    def time_mark(self):
        """Marca de tempo da entrada deste cliente na agência"""
        return self._time_mark

    def get_wait_time(self, local_time):
        """Tempo de espera na fila deste cliente em segundos"""
        return (local_time - self._time_mark).seconds

####################### Class CashTerminal #################################


class CashTerminal(QueueP2):
    """Classe da abstração terminal de autoatendimento"""

    def __init__(self, parent, label):
        """Construtor recebe rótulo deste terminal(sem validação de unicidade)"""
        super().__init__()
        self._label = label
        self._parent = parent
        return

    @property
    def label(self):
        """Rótulo do terminal"""
        return self._label

    @property
    def avg_wait_time(self):
        if( self.count > 0 ):
            sum = 0
            for c in self.queue:
                sum += c.get_wait_time( self._parent.local_time )
            return ( sum / self.count )
        else:
            return 0

    @property
    def max_wait_time(self):
        ret = 0
        for c in self.queue:
            if( c.get_wait_time( self._parent.local_time ) > ret ):
                ret = c.get_wait_time( self._parent.local_time )
        return ret

    def get_max_wait_time(self, current_time):
        """Tempo máximo de espera dos clientes neste terminal em segundos"""
        ret = 0
        for client in self.queue:
            if(ret < client.get_wait_time(current_time)):
                ret = client.get_wait_time(current_time)
        return ret

    def incoming_client(self, client):
        """Aceita cliente na fila deste terminal. Retorna a quantidade de clientes atualmente na fila"""
        self.insert_data(client)
        return len(self.queue)

    # Recebe a quantidade de clientes a serem processados e retorna a quantidade efetivamente processada
    def process_clients(self, count):
        """Evento de processamento dos clientes na fila. Extrai a quantidade informada como argumento"""
        ret = 0
        for _ in range(count):
            if( self.remove_data() is not None ):
                ret += 1
        return ret

    def remove_data(self):
        """Remove o primeiro cliente da fila, retornando o mesmo ou None caso fila vazia"""
        if(self.count > 0):
            return super().remove_data()
        else:
            return None

    def get_total_queue_time(self, local_time):
        """Tempo total de espera de todos os clientes em segundos"""
        ret = 0
        for client in self.queue:
            ret += client.get_wait_time(local_time)
        return ret

#####################  Class BankAgency #########################


class BankAgency(object):
    """Abstração de agência bancária"""

    def __init__(self, terminal_count, time):
        """Construtor da agência.
        terminal_count -> Quantidade de terminais existentes
        time -> Marca de tempo atual
        """
        super().__init__()
        self._terminals = []
        self._local_time = time
        for term_count in range(terminal_count):
            self._terminals.append(CashTerminal(self, term_count))
        return

    @property
    def terminals(self):
        """Lista de terminais presentes na agência"""
        return self._terminals

    @property
    def local_time(self):
        """Marca de tempo "ATUAL" da simulação"""
        return self._local_time

    @property
    def client_count(self):
        """Quantidade total de clientes presentes na agência"""
        ret = 0
        for term in self._terminals:
            ret += term.count
        return ret

    @property
    def avg_wait_time(self):
        """Tempo médio(segundos) de espera de todos os clientes presentes"""
        total_time = 0
        client_count = 0
        for terminal in self._terminals:
            total_time += terminal.get_total_queue_time(self._local_time)
            client_count += terminal.count
        if(client_count > 0):  # validar o resultado
            return total_time/client_count
        else:
            return 0

    @property
    def max_wait_time(self):
        """Tempo máximo de espera do cliente mais azarado"""
        ret = 0
        for term in self._terminals:
            if(ret < term.get_max_wait_time(self._local_time)):
                ret = term.max_wait_time
        return ret

    def increment_time(self, delta):
        """Incrementa o tempo simulado pela quantidade de minutos informada como argumento"""
        minutes = timedelta(0, 0, 0, 0, delta)
        self._local_time = self._local_time + minutes
        return self._local_time

    def accept_client(self):
        """Registra a entrada de novo cliente e redireciona ao terminal de menor fila"""
        cash_terminal = self.prior_terminal
        client = Client(self.local_time)
        cash_terminal.incoming_client(client)
        return client

    @property
    def prior_terminal(self):
        """Varre lista de caixas e retorna qual terminal tem menos clientes no momento"""
        ret = self._terminals[0]
        for terminal in self._terminals:
            if terminal.count < ret.count:  # Terminal com menos clientes dentre os existentes
                ret = terminal
        return ret

    def outcoming_clients(self, max_client_count):
        """Dispara e processa o evento de atendimento para todos os terminais. 
        Retorna a quantidade total de clentes atendidos neste ciclo.
        max_client_count -> Máximo de clientes atentidos por terminal em cada ciclo
        """
        out = 0
        for c in self._terminals:
            # remover clientes entre 1 e 2
            out += c.process_clients(random.randint(1, max_client_count))
        return out

    def incoming_clients(self, min_client_count, max_client_count):
        """Dispara e processa o evento de entrada de clientes na agência.
        min_client_count -> mínimo de clientes por ciclo
        max_client_count -> máximo de clientes por ciclo
        Retorna a quantidade total de clientes entrantes neste ciclo
        """
        incoming_count = random.randint(min_client_count, max_client_count)
        for cc in range(incoming_count):
            self.accept_client()
        return incoming_count


############### Class SimMediator  ######################

class SimMediator(object):
    """Classe de controle da simulação"""

    def __init__(self, terminal_count, min_clients_per_cycle, max_clients_per_cycle, max_clients_per_terminal):
        """Instancia um controlador da simulação e demais elementos internos
        min_clients_per_cycle: Mínimo clientes entrantes por ciclo
        max_clients_per_cycle: Máximo clientes entrantes por ciclo
        max_clients_per_terminal: Mínimo clientes saintes por ciclo para cada terminal
        """
        super().__init__()
        self._local_time = datetime.now()
        self._agency = BankAgency(terminal_count, self._local_time)
        self._min_clients_per_cycle = min_clients_per_cycle
        self._max_clients_per_cycle = max_clients_per_cycle
        self._max_clients_per_terminal = max_clients_per_terminal
        self._cycle_count = 0
        self._cycle_incoming = 0
        self._cycle_outcoming = 0

    @property
    def cycle_incoming(self):
        """Quantidade de clientes entrantes no ciclo atual da simulação"""
        return self._cycle_incoming

    @property
    def cycle_outcoming(self):
        """Quantidade de clientes saintes no ciclo atual da simulação"""
        return self._cycle_outcoming

    @property
    def cycle_count(self):
        """Contador de ciclos executados"""
        return self._cycle_count

    @property
    def local_time(self):
        """Marca de tempo simulado(diferente do tempo real)"""
        return self._local_time

    @property
    def agency(self):
        """Agência da simulação"""
        return self._agency

    def do_cycle(self):
        """Dispara e processa o evento de ciclo de simulação, incrementando o tempo em 1 minuto"""
        self._cycle_count += 1  #Contador de ciclos
        self._agency.increment_time(1)  # tempo em minutos
        self._cycle_incoming = self._agency.incoming_clients(self._min_clients_per_cycle, self._max_clients_per_cycle )
        self._cycle_outcoming = self._agency.outcoming_clients( self._max_clients_per_terminal )
        return
