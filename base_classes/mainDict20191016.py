"""
dicionario de nome para data nascimento e endereço completo
"""

from datetime import datetime

import itertools


def insert_item( dic, name, birt, address):
    dic[ name ] = [ birt, address ]

def main():
    dic = {}
    insert_item( dic, 'Eu', datetime( 1990, 12, 2), 'Rua dos bobos, 0')
    insert_item( dic, 'Tu', datetime( 1990, 12, 2), 'Rua dos bobos, 0')
    insert_item( dic, 'Ele', datetime( 1990, 12, 2), 'Rua dos bobos, 0')
    insert_item( dic, 'Nos', datetime( 1990, 12, 2), 'Rua dos bobos, 0')
    insert_item( dic, 'Vos', datetime( 1990, 12, 2), 'Rua dos bobos, 0')
    insert_item( dic, '2', datetime( 1990, 12, 2), 'valor de 2')
    
    lixo = next( dic )
    print( lixo )

    print( dic )

    if 2 in dic:
        print( 'Valor de 2 encontrado')

main()

