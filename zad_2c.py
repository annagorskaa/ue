def zad_2c(liczby: list):

    for n in range(len(liczby)):
        if liczby[n] % 2 == 0:
            print(liczby[n])


if __name__ == '__main__':
    liczby = [1, 2, 4, 4, 5, 6, 13, 8, 12, 3]
    zad_2c(liczby)
