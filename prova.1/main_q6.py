from my_queue import ProofQueue



def parentesis_balanced( s ):
    q = ProofQueue()
    ptr = 0
    fail_point = 0
    last_open = 0
    for ptr in range( len( s ) ):
        char = s[ptr]
        if char == '(':
            q.push(ptr)
            last_open = ptr
        if char == ')':
            try:
                q.pop()
            except:
                fail_point = ptr
    if q.size != 0:
        return last_open
    else:
        return fail_point


def main( argv ):
    """A partir de uma string de entrada, verificar se a mesma está balanceada"""
    if ''.__eq__( argv ):
        in_str = input( 'Informe a cadeia a ser analisada: ')
    else:
        in_str = argv
    err_point = parentesis_balanced( in_str )
    if( err_point == 0 ):
        print( 'Cadeia balanceada')
    else:
        print( f'Cadeia desbalanceada no caracter: { err_point }')
    


main( '(ssfd sd f)((ok)ok---(sd))(' )