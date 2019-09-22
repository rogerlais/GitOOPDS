def CalcAvg(v1, v2):
    return (v1 + v2)/2


def ExercA():
    ar = [0, 1, 2, 3, 4]
    ar.insert(3, 100)
    for n in ar:
        print(4*n)


def ExercB():
    list = []
    item = ""
    while(item != None):
        item = input("informe o valor(branco para terminar)")
        if ("" == item):
            item = None
        else:
            list.append(item)
    return list

def readArray( ar, clean, caption, prompt, maxLen ):
    if clean :
        ar.clear()
    if None != maxLen :
        #coleta valores até valor em branco ser informado
        item = None
        while ( "" != item ):
            
        #fim
    else:
        #Coleta valores até tamamnho atiginr limite
    #fim teste
#fim func

def main():
    import colorama
    import sys
    funcdict = {
        'readArray': readArray
    }


funcdict[myvar](parameter1, parameter2)
print(ExercB())


main()
