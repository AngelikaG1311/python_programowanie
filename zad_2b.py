#zadanie 2b i.#
def podwajanie(lista_liczb):
    for liczba in lista_liczb:
        podwojona=liczba*2
        print(podwojona)

lista=[3,1,8,9,4]
podwajanie(lista)

#zadanie 2b ii.#
def podwajanie (lista_liczb):
    return [x*2 for x in lista_liczb]

lista=[5,10,15,20,25]
wynik=podwajanie(lista)
print(wynik)