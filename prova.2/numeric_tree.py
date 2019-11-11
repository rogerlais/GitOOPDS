import sys
import os.path as path
from inspect import getsourcefile
current_dir = path.dirname(path.abspath(getsourcefile(lambda: 0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from base_classes.tree import Node, BinaryTree

class NumericTree( BinaryTree ):
    def __init__( self ):
        super( NumericTree, self ).__init__( )
