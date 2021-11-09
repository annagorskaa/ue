def zad_5(li: list, number: int) -> bool:
    return number in li


if __name__ == '__main__':
    text = ['aha', 3, 4, 5, 'meh', 'test']
    print(zad_5(text, 5))
