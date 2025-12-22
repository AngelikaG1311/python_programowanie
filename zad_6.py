def nowa_lista(lista1, lista2):
    polaczenie = lista1 + lista2
    unikat = set(polaczenie)
    nowa = [x**3 for x in unikat]
    return nowa


lista1 = [1, 3, 5]
lista2 = [2, 4, 6]
wynik = nowa_lista(lista1, lista2)
print(wynik)
