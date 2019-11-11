#! coloca o diretorio pai no path de imports
# Dica de https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
import time
from numeric_tree import NumericTree
from binary_file_system import TreeDirectory
import sort_methods
from timeit import default_timer as timer
from random import randint
import os
from inspect import getsourcefile
import os.path as path
import sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda: 0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from base_classes.linked_list import SimpleLinkedList

# Imports

sys.path.pop(0)  # Remocao opcional após importação


def show_array(arr):
    """Exibe array no limite de um tela de 80 colunas"""
    s = '['
    x = 0
    while (len(s) < 80) and (x < len(arr)):
        s += str(arr[x]) + ', '
        x += 1
    if len(arr) > x:
        s = s.strip(', ') + ',...]'
    else:
        s = s.strip(', ') + ']'
    print(s)
    return


def gen_data():
    """Gera os dados simulados para as operções de ordenação"""
    arr08 = [8, 6, 3, 7, 84, 9, 6, 31]
    arr10 = [2, 3, 1, 3, 4, 3, 3, 3, 5, 3]
    arr11 = [38, 27, 43, 3, 9, 0, -26, 27, 9, 82, 10]
    arr13 = [5, -26, 38, 27, 43, 3, 9, 0, -26, 27, 9, 82, 10]
    random_array = [randint(0, 100000) for _ in range(1000)]
    data = [arr08, arr10, arr11, arr13, random_array]
    return data


def test_sort_method(data, sort_call=lambda arr, flag, sorting: (arr, flag)[sorting]):
    print('Dados de entrada:')
    for x in range(len(data)):
        show_array(data[x])
    rets = []
    start = timer()
    for x in range(len(data)):
        rets.append(sort_call(data[x], True))
        #rets.append( sort_methods.merge_sort(data[x], True) )
    end = timer()
    exectime = (end - start)
    print('Dados de saída:')
    for x in range(len(rets)):
        show_array(rets[x])
    print(f'Tempo de execução: { exectime }')


def first_question():

    print( "Execução da primeira questão:")

    # merge_sort
    data = gen_data()
    print('MERGE SORT')
    test_sort_method(data, sort_methods.merge_sort)

    # Bubble sort
    print("BUBBLE SORT")
    data = gen_data()
    test_sort_method(data, sort_methods.bubbleSort)

    # Insertion sort
    print('INSERTION SORT')
    data = gen_data()
    test_sort_method(data, sort_methods.insertion_sort)

    # TimSort
    print('TIM SORT')
    data = gen_data()
    test_sort_method(data, sort_methods.timsort)


def generate_linkedlists():
    """Gera array com 2 listas simplesmente encadeadas"""
    l1 = SimpleLinkedList()
    l1.add_value(5)
    l1.add_value(10)
    l1.add_value(15)
    l2 = SimpleLinkedList()
    l2.add_value(2)
    l2.add_value(3)
    l2.add_value(20)
    return [l1, l2]


def merge_linked_list(lnklist1, lnklist2, ascending=True):
    """Recebe duas listas encadeads, ambas ordenadas, e faz o merge delas"""
    # Uma nova lista será gerada, nada impede de movermos os nos, esvaziando as listas de entrada
    ret = SimpleLinkedList()
    ptl = lnklist1.head
    ptr = lnklist2.head
    def compare(x, y, ascending): return (x > y, x < y)[ascending]
    while ((ptl != None) and (ptr != None)):  # Varre os lados em // adicionando os menores/maiores de acordo com compare
        if compare(ptl.value, ptr.value, ascending):
            ret.add_value(ptl.value)
            ptl = ptl.next
        else:
            ret.add_value(ptr.value)
            ptr = ptr.next
    while (ptl != None):  # Adiciona os elementos faltantes de um dos outros lados
        ret.add_value(ptl.value)
        ptl = ptl.next
    while (ptr != None):
        ret.add_value(ptr.value)
        ptr = ptr.next
    return ret


def second_question():
    print( "Execução da primeira questão:")

    chain_lists = generate_linkedlists()
    merged_list = merge_linked_list(chain_lists[0], chain_lists[1])
    print(merged_list)
    return

def third_question(interactive=False):

    print( "Execução da terceira questão:")
    DATE_FORMAT = "%d/%m/%Y-%H:%M:%S"
    if interactive:
        dir = input("Informe o caminho a ser carregado(nulo = atual):")
        limit = input( f'Informe a data/hora limite para remoção({DATE_FORMAT})')
        dtLimit = time.strptime( limit ,  DATE_FORMAT)
    else:
        dir = ''
        dtLimit = time.strptime( "05/11/2019-22:00:00" ,  DATE_FORMAT)
    if dir == '':
        dir = os.path.dirname(os.path.abspath(__file__))
    print("Caminho a ser carregado: ", dir)
    bt = TreeDirectory(dir)  # Cria e inicia o no raiz
    #bt.insert_value( dir )
    bt.load_from_path(None, False)
    bt.root_node.display()
    bt.purge( time.mktime( dtLimit ) )
    bt.root_node.display()


def fourth_question():

    print( "Execução da quarta questão:")

    nt1 = NumericTree()
    nt1.insert_value(7)
    nt1.insert_value(8)
    nt1.insert_value(3)
    nt1.insert_value(4)
    nt1.insert_value(2)
    nt1.insert_value(1)
    nt1.insert_value(6)
    nt1.insert_value(5)

    nt2 = NumericTree()
    nt2.insert_value(7)
    nt2.insert_value(8)
    nt2.insert_value(3)
    nt2.insert_value(4)
    nt2.insert_value(2)
    nt2.insert_value(1)
    nt2.insert_value(6)
    nt2.insert_value(5)

    nt1.root_node.display()
    nt2.root_node.display()
    if nt1.is_similar( nt2 ):
        print( "POSITIVO: Árvores são similares")
    else:
        print( "NEGATIVO: Árvores não são similares")

    nt2.insert_value( 10 )
    nt1.root_node.display()
    nt2.root_node.display()
    if nt1.is_similar( nt2 ):
        print( "POSITIVO: Árvores são similares")
    else:
        print( "NEGATIVO: Árvores não são similares")

    return

def fifth_question():
    print( "Execução da quinta questão")
    nt = NumericTree()
    nt.insert_value(7)
    nt.insert_value(8)
    nt.insert_value(3)
    nt.insert_value(4)
    nt.insert_value(2)
    nt.insert_value(1)
    nt.insert_value(6)
    nt.insert_value(5)
    nt.root_node.display()

    seq = nt.inorder()
    step = 0
    for item in seq:
        step += 1
        print( f'Em ordem - Passo { step }')
        item.selected = True
        nt.root_node.display()
        item.selected = False

    seq = nt.preorder()
    step = 0
    for item in seq:
        step += 1
        print( f'Em pre-ordem - Passo { step }')
        item.selected = True
        nt.root_node.display()
        item.selected = False

    seq = nt.postorder()
    step = 0
    for item in seq:
        step += 1
        print( f'Em pos-ordem - Passo { step }')
        item.selected = True
        nt.root_node.display()
        item.selected = False
    
    #Removendo elementos 7 e 6
    nt.remove( 7 )
    nt.remove( 6 )

    #Exibição após remoção
    seq = nt.preorder()
    step = 0
    for item in seq:
        step += 1
        print( f'Em pre-ordem, excluidos( 7 e 6 ) - Passo { step }')
        item.selected = True
        nt.root_node.display()
        item.selected = False
    return


def main():
    first_question()  #Test Sort Methods

    second_question() #MergeSort to LinkedLists

    third_question( True ) #BinaryFileSystem arg-interative -> prompts para argumentos

    fourth_question() #Compare trees

    fifth_question() #BinaryTree orders/remove


main()
