from base_classes.mtree import OperBinaryTree, OperNode


def main():
    #root = BinaryTree( 1, BinaryTree( 2 ), BinaryTree( 3 ) )
    root = OperBinaryTree()
    root.insert_node(OperNode('='))
    rn = root.root_node
    print( rn.__class__ )
    rn.create_operation('+', 2, 2)
    print(rn.display())
    print(rn.merge())

    '''
    print( 'Enumeração - inorder')
    for n in node.traversal_inorder():
        print ( n )

    print( 'Possui ', root.levels(), 'niveis')
    print( 'Possui ', root.childnodes, 'filhos')
    print( 'Possui ', root.leafs, 'folhas')
    '''


main()


# nvmo - telefonia móvel
