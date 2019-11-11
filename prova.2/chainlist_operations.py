from inspect import getsourcefile
import os.path as path
import sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda: 0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from base_classes.linked_list import SimpleLinkedList  # Replace "my_module" here with the module name.
sys.path.pop(0)  # Remocao opcional após importação


def merge_chain_lists( l1, l2 ):
    first = l1.Node
    sec = l2.Node
    