def zad_2d(lista: list):
    for n, l in enumerate(lista):
        if n % 2 == 0:
            continue
        print(l)


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    zad_2d(lista)
