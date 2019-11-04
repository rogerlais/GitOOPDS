from my_queue import ProofQueue

def is_palindrome( s ):
    q = ProofQueue()
    for c in s:
        q.push( c )
    reverse = ''
    for x in range( q.size ):
        reverse += q.pop()
    return reverse.__eq__( s )



def main( argv ):
    if ''.__eq__( argv ):
        in_str = input( 'Informe a cadeia a ser testada: ')
    else:
        in_str = argv
    ret = is_palindrome( in_str )
    if ret :
        print( 'cadeia é palindoromo')
    else:
        print( 'Cadeia não é palindromo')



main( 'arara2')