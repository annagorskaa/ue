from klasy.Zamowienie import Zamowienie
from klasy.Developer import Developer
from klasy.Nieruchomosc import Nieruchomosc

if __name__ == '__main__':
    zam = Zamowienie()
    zam.developer = Developer('Jan', 'Kowalski', 32, 6)
    zam.lista_nieruchomosci = [Nieruchomosc('Katowice', 'Mikołowska', 100, 255),
                               Nieruchomosc('Gliwice', 'Dobra', 30, 100)]
    zam.data = '25-11-2021'
    zam.numer_zamowienia = 225461

    print(zam)