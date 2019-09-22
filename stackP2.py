'''
Name conventions based at: 
https://www.python.org/dev/peps/pep-0008/#package-and-module-names
Python perdeu 20 pontos com isso para mim :(
'''

class StackP2( object ):
    def __init__( self ):
        self.data = []
    
    #insert item
    def push(self, item):
        self.data.append( item )
        return self.data.count
    
    def pop(self):
        return self.data.pop()
    
    def get_data(self):
        return self.data

    def peek(self):
        if( self.data.count > 0 ):
            return self.data[ self.data.count - 1 ]
        else:
            return None

    def clear(self):
        self.data = []

    def equals_didatic( self, st ):
        ret = ( len( self.data ) == len( st.getData() ) )
        pointer = 0
        while( ret and ( len(self.data) > pointer )  ):
            ret = ( self.data[ pointer ] == st.getData()[pointer])
            pointer += 1
        return ret

    def equals_pratical( self, st ):
        return self.get_data() == st.get_data()
