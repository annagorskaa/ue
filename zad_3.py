def zad_3(number: int) -> bool:
    x = number % 2 == 0
    if x:
        print('Liczba parzysta')
    else:
        print('Liczba nieparzysta')


if __name__ == '__main__':
    zad_3(5)
