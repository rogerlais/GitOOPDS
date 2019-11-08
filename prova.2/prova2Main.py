#! coloca o diretorio pai no path de imports 
#Dica de https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder
from inspect import getsourcefile
import os.path as path, sys
current_dir = path.dirname(path.abspath(getsourcefile(lambda:0)))
sys.path.insert(0, current_dir[:current_dir.rfind(path.sep)])
from base_classes.linked_list import SimpleLinkedList  # Replace "my_module" here with the module name.
sys.path.pop(0)  #Remocao opcional após importação

"""
sys.path.append('..')
print( sys._base_executable )
"""



def main():
    # ar = [ 8,6,3,7,84,9,6,31]
    # arr = [2, 3, 1, 3, 4, 3, 3, 3, 5, 3]
    """
    arr = [38, 27, 43, 3, 9, 0, -26, 27, 9, 82, 10]
    print(merge_sort(arr, False))
    arr = [38, 27, 43, 3, 9, 0, -26, 27, 9, 82, 10]
    print(bubbleSort(arr))
    """
    arr = [5, -26, 38, 27, 43, 3, 9, 0, -26, 27, 9, 82, 10]
    print(arr)
    # print(insertion_sort(arr))
    #print(quicksort(arr, False))
    print(timsort(arr))


def merge(left, right, ascending, compare):
    """Une as partes separadas de volta"""
    ret = []
    ptl = 0
    ptr = 0
    while ((ptl < len(left)) and (ptr < len(right))):  # Varre os lados em // adicionando os menores/maiores de acordo com compare
        if compare(left[ptl], right[ptr], ascending):
            ret.append(left[ptl])
            ptl += 1
        else:
            ret.append(right[ptr])
            ptr += 1
    while (ptl < len(left)):  # Adiciona os elementos faltantes de um dos outros lados
        ret.append(left[ptl])
        ptl += 1
    while (ptr < len(right)):
        ret.append(right[ptr])
        ptr += 1
    return ret


def merge_sort(arr, ascending=True, compare=lambda x, y, asc: (x > y, x < y)[asc]):
    """Compara os elementos através da lambda(X < y ) significa ordem crescente)"""
    if len(arr) < 2:
        return arr[:]
    else:
        center = len(arr) // 2
        larr = merge_sort(arr[:center], ascending, compare)
        rarr = merge_sort(arr[center:], ascending, compare)
        return merge(larr, rarr, ascending, compare)


def bubbleSort(data, ascending=True):
    size = len(data)
    for dir in range(size):  # Percurso direto
        for rev in range(0, size-dir-1):  # Percurso reverso
            if(ascending):
                if data[rev] > data[rev+1]:
                    data[rev], data[rev+1] = data[rev+1], data[rev]
            else:
                if data[rev] < data[rev+1]:
                    data[rev], data[rev+1] = data[rev+1], data[rev]
    return data


def insertion_sort(data):
    """Efetua ordenação pelo método de inserção"""
    for i in range(1, len(data)):
        item_to_insert = data[i]
        j = i - 1  # index do elemento anterior
        while j >= 0 and data[j] > item_to_insert:  # Move all items of the sorted segment forward if they are larger than the item to insert
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = item_to_insert  # Insere o item
    return data


def quicksort(data, ascending=True):
    if(len(data) > 1):
        pivotIdx = int(len(data)/2)
        pivotal_value = data[pivotIdx]
        middleData = [i for i in data if i == pivotal_value]  # agrupa elementos iguais ao valor pivotal
        minorData = [i for i in data if i < pivotal_value]  # agrupa elementos menores que valor pivotal
        majorData = [i for i in data if i > pivotal_value]  # agrupa elementos maiores que valor pivotal
        if ascending:
            ret = quicksort(minorData, ascending) + middleData + quicksort(majorData, ascending)  # Junta as partes menor para maior
        else:
            ret = quicksort(majorData, ascending) + middleData + quicksort(minorData, ascending)   # Junta as partes maior para menor
        return ret
    else:
        return data


def timsort(data, ascending=True):
    def compare(x, y, asc): return (x > y, x < y)[asc]
    runs, sorted_runs = [], []
    dataSize = len(data)
    new_run = [data[0]]
    for i in range(1, dataSize):  # do segundo ao último
        if i == dataSize - 1:  # Atingido o final da lista
            new_run.append(data[i])
            runs.append(new_run)
            break
        if data[i] < data[i-1]: # testa i-ésimo elemento do arranjo < anterior 
            if not new_run:  # testa new_run not NULL
                runs.append([data[i]])
                new_run.append(data[i])
            else:
                runs.append(new_run)
                new_run = [data[i]]
        else:  # else if its equal to or more than
            new_run.append(data[i])
    for item in runs: # para todo elemento em runs, agrega usando insert_sort
        sorted_runs.append(tim_insertion_sort(item))

    # para todo arranjo run em sorted_runs, efeuta o merge
    sorted_array = []
    for run in sorted_runs:
        sorted_array = tim_merge(sorted_array, run)  # , ascending, compare )
    return sorted_array


def tim_merge(left, right):  # método auxiliar para unir dois arranjos comparando os elementos por vez [1, 2, 3, 4, 5, 6]
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + tim_merge(left[1:], right)
    return [right[0]] + tim_merge(left, right[1:])


def tim_insertion_sort(the_array):
    l = len(the_array)
    for index in range(1, l):
        value = the_array[index]
        pos = tim_binary_search(the_array, value, 0, index - 1)
        the_array = the_array[:pos] + [value] + the_array[pos:index] + the_array[index+1:]
    return the_array


def tim_binary_search(the_array, item, start, end):
    if start == end:
        if the_array[start] > item:
            return start
        else:
            return start + 1
    if start > end:
        return start

    mid = round((start + end) / 2)  # ? não usar //?

    if the_array[mid] < item:
        return tim_binary_search(the_array, item, mid + 1, end)
    elif the_array[mid] > item:
        return tim_binary_search(the_array, item, start, mid - 1)
    else:
        return mid


main()
