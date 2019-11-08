from base_classes.tree import BinaryTree

def main():
    root = BinaryTree( 1, BinaryTree( 2 ), BinaryTree( 3 ) )
    root.insert( 4 )
    node = root.findLinear( 1 )

    print( 'Enumeração - inorder')
    for n in node.traversal_inorder():
        print ( n )

    print( 'Possui ', root.levels(), 'niveis')
    print( 'Possui ', root.childnodes, 'filhos')
    print( 'Possui ', root.leafs, 'folhas')

    print( root.toPlainText(80))

main()



# nvmo - telefonia móvel
