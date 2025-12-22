def parzysta(lista_liczb):
    for liczba in lista_liczb:
        if liczba % 2 ==0:
            print(liczba)

lista=list(range(1,11))
parzysta(lista)

