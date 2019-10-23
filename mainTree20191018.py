from base_classes.tree import BinaryTree

def main():
    root = BinaryTree( 1, BinaryTree( 2 ), BinaryTree( 3 ) )

    node = root.findLinear( 1 )

    print( node )

    for n in node.traversal_inorder():
        print ( n )

main()



# nvmo - telefonia móvel
