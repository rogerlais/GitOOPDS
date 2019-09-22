import queueP2

def insert_exerC( queue ) :
    queue.insertData( 0 )
    queue.insertData( 0 )
    queue.insertData( 0 )
    queue.insertData( 0 )
    return

def main():
    qTest = queueP2.QueueP2()
    print( qTest.get_queue() )
    qTest.insert_data( 2 )
    insert_exerC( qTest )
    qTest.remove_data()
    return


##### ponto de entrada  ####
main()

