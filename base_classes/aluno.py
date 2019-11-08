class Aluno(object):

    def __init__(self, name, enrollment, address, cpf ):
        """nome, matricula, endereço e cpf"""
        self.__name = ''
        self.__enrollment = enrollment
        self.__address = address
        self.__cpf = cpf
        return

    def get_name( self ):
        return self.__name

    def set_name( self, newname ):
        self.__name = newname
        return

    name = property( get_name, set_name )
