import stackP2


def insert_provinces(st):
    st.push('rio grande do norte')
    st.push('maranhão')
    st.push('piaui')
    st.push('ceará')
    st.push('pernambuco')
    st.push('paraíba')
    return st


def input_itens(ss):
    newItem = input('Informe o valor a ser inserido: ')
    while(newItem != ''):
        ss.push(newItem)
        newItem = input('Informe o valor a ser inserido: ')


def main():
    s1 = stackP2.StackP2()
    s2 = stackP2.StackP2()
    #input_itens( s1 )
    #input_itens( s2 )
    insert_provinces(s1)
    insert_provinces(s2)
    print(f'As pilhas com relação a equidade(modo didático) = { s1.equals_didatic( s2 ) }')
    print(f'As pilhas com relação a equidade(modo prático) = { s1.equals_pratical( s2 ) }')


main()
