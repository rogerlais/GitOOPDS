#import sys
#sys.path.insert(0, './GitOOPDS/QueueExerc')
import QueueExerc.bank_classes  #import bank_classes

def init_simulation():
    #carrega lista de caixas
    agency = QueueExerc.bank_classes.BankAgency(5)
    return agency


def generate_report(incoming, outcoming, agency):
    print( f'Neste ciclo chegaram { incoming } clientes')
    print( f'Neste ciclo sairam { outcoming } clientes')
    print( f'Neste ciclo chegaram { agency.get_avg_wait_time() } clientes')
    return


def main():
    agency = init_simulation()
    #Inicia simulação temporal por timeslice de 1 minuto, onde podem entrar de 4 a 16 clientes e sair de 1 a 2 clientes pode caixa
    repeat_step = True
    while( repeat_step ):
        incoming = agency.incoming_clients()
        outcoming = agency.outcoming_clients()
        generate_report(incoming, outcoming, agency )
        repeat_step = input( 'Deseja repetir a simulação?(S/N): ').upper() == 'S'
    return


######################### PONTO DE ENTRADA  #########################
main()