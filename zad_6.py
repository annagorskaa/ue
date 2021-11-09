def zad_6(one: list, two: list) -> list:
    together = []
    for n in list(set(one+two)):
        n = n**3
        together.append(n)
    return together


if __name__ == '__main__':
    p = [2, 5, 7]
    d = [1, 3, 10, 2]

    print(zad_6(p, d))
