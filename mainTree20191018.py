from base_classes.tree import BinaryTree

def main():
    root = BinaryTree( 1, BinaryTree( 2 ), BinaryTree( 3 ) )

    node = root.findLinear( 1 )

    print( node )

main()



# nvmo - telefonia móvel
