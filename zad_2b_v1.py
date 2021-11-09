def zad_2b(lista: list):
    mnozenie = []
    for n in lista:
        mnozenie.append(n*2)
        return mnozenie


if __name__ == '__main__':
    lista = [1, 2, 5, 4, 6]
    print(zad_2b(lista))
