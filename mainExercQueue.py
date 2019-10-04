import curses
import os
import sys
import colorama
import builtins
import time
#sys.path.insert(0, './GitOOPDS/QueueExerc')
from QueueExerc.bank_classes import SimMediator, BankAgency, CashTerminal, Client  # import bank_classes
import msvcrt
from datetime import datetime, timedelta


def init_simulation():
    # carrega lista de caixas
    agency = BankAgency(5, datetime.now())
    return agency


def printMatrix(s):
    # Do heading
    print("     ", end="")
    for j in range(len(s[0])):
        print("%5s " % j, end="")
    print()
    print("     ", end="")
    for j in range(len(s[0])):
        print("------", end="")
    print()
    # Matrix contents
    for i in range(len(s)):
        print("%3s |" % (i), end="")  # Row nums
        for j in range(len(s[0])):
            print("%5s " % (s[i][j]), end="")
        print()


def show_report(control):
    print('')
    print(f'Hora simulada:{ control.local_time }       Ciclo#: {control.cycle_count}')
    print(f'Neste ciclo chegaram: { control.cycle_incoming } clientes')
    print(f'Neste ciclo sairam  : { control.cycle_outcoming } clientes')
    print(f'Existem { control.agency.client_count } clientes na agência')
    print('TEMPOS:')
    avg_time = control.agency.avg_wait_time
    str_avg = f'{ avg_time // 60 } minutos e { avg_time % 60 } segundos'
    max_time = control.agency.max_wait_time
    str_max = f'{ max_time // 60 } minutos e { max_time % 60 } segundos'
    print(f'Tempo médio: { str_avg }    Tempo máximo: { str_max } ')
    report_array = []
    report_array.append(['Caixa', 'Clientes', 'Média', 'Máximo'])
    for term in control.agency.terminals:
        report_array.append([term.label, term.count, term.avg_wait_time, term.max_wait_time])
    #print('\n'.join([str(n) + ":  " + str(entry) for (n, entry) in zip(range(0, len(report_array)), report_array)]))
    printMatrix( report_array )
    return


def get_user_continue():
    print('Deseja repetir a simulação?(S/N): ', end='')
    key = bytes('Z', 'utf-8')
    while(not(key.decode().upper() in ['S', 'N'])):
        if msvcrt.kbhit():
            key = msvcrt.getch()
            print(key.decode(), end='')   # just to show the result
    return (key.decode().upper() == 'S')


def main():
    simulator = SimMediator(5, 4, 16, 2)
    # Inicia simulação temporal por timeslice de 1 minuto, onde podem entrar de 4 a 16 clientes e sair de 1 a 2 clientes pode caixa
    repeat_step = True
    while(repeat_step):
        simulator.do_cycle()
        show_report(simulator)
        time.sleep(1)
        repeat_step = get_user_continue()
    print('SIMULAÇÃO FINALIZADA PELO OPERADOR!')
    return    



######################### PONTO DE ENTRADA  #########################
main()
