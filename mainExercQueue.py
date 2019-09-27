import curses
import os
import sys
import colorama
import builtins
import time
#sys.path.insert(0, './GitOOPDS/QueueExerc')
import QueueExerc.bank_classes  #import bank_classes
import msvcrt
from datetime import datetime, timedelta

def init_simulation():
    #carrega lista de caixas
    agency = QueueExerc.bank_classes.BankAgency(5, datetime.now() )
    return agency


def generate_report(incoming, outcoming, agency):
    print( f'Neste ciclo chegaram { incoming } clientes')
    print( f'Neste ciclo sairam { outcoming } clientes')
    print( f'Neste ciclo chegaram { agency.get_avg_wait_time() } clientes')
    return

def get_user_continue():
    print( 'Deseja repetir a simulação?(S/N): ', end='')
    key = bytes( 'Z', 'utf-8' )
    while( not( key.decode().upper() in ['S', 'N'] )):
       if msvcrt.kbhit():
           key = msvcrt.getch()
           print(key.decode(), end='')   # just to show the result
    return ( key.decode().upper() == 'S' )


def main():
    agency = init_simulation()
    #Inicia simulação temporal por timeslice de 1 minuto, onde podem entrar de 4 a 16 clientes e sair de 1 a 2 clientes pode caixa
    repeat_step = True
    while( repeat_step ):
        agency.increment_time( 1 )
        incoming = agency.incoming_clients()
        outcoming = agency.outcoming_clients()
        generate_report(incoming, outcoming, agency )
        time.sleep(1)
        repeat_step = get_user_continue()
    return


######################### PONTO DE ENTRADA  #########################
#value = int(raw_input("Enter the inputs : ") or "42")

main()