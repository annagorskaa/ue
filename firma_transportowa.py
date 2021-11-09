class Firma:
    def __init__(self, nazwa: str, rodzaj: str, miasto: str, ulica: str, numer: int):
        self._nazwa = nazwa
        self._rodzaj = rodzaj
        self._miasto = miasto
        self._ulica = ulica
        self._numer = numer

    @property
    def nazwa(self) -> str:
        return self._nazwa

    @property
    def rodzaj(self) -> str:
        return self._rodzaj

    @property
    def miasto(self) -> str:
        return self._miasto

    @property
    def ulica(self) -> str:
        return self._ulica

    @property
    def numer(self) -> int:
        return self._numer

    def __str__(self):
        return f'Firma: "{self._nazwa}", ' \
               f'z branży: {self._rodzaj} ' \
               f'siedziba: {self._miasto} {self._ulica} {self._numer}'


class FirmaTransportowa(Firma):
    def __init__(self, nazwa: str, rodzaj: str, miasto: str, ulica: str, numer: int, region: str) -> None:
        super().__init__(nazwa, rodzaj, miasto, ulica, numer)
        self._region = region

    @property
    def region(self) -> str:
        return self._region

    def __str__(self):
        return f''


class FirmaSpozywcza(Firma):
    def __init__(self, nazwa: str, rodzaj: str, miasto: str, ulica: str, numer: int, eko: str) -> None:
        super().__init__(nazwa, rodzaj, miasto, ulica, numer)
        self._eko = eko

    @property
    def eko(self) -> str:
        return self._eko


class Pojazd:
    def __init__(self, marka: str, kolor: str, rocznik: int, numer_rejestr: str, typ: str):
        self._marka = marka
        self._kolor = kolor
        self._rocznik = rocznik
        self._numer_rejestr = numer_rejestr
        self._typ = typ

    @property
    def marka(self) -> str:
        return self._marka

    @property
    def kolor(self) -> str:
        return self._kolor

    @property
    def rocznik(self) -> int:
        return self._rocznik

    @property
    def numer_rejestr(self) -> str:
        return self._numer_rejestr

    @property
    def typ(self) -> str:
        return self._typ

    def __str__(self):
        return f'Pojazd: ' \
               f'marki: {self._marka}' \
               f'w kolorze {self._kolor} ' \
               f'rocznik: {self._rocznik}' \
               f'numer rejestracyjny {self._numer_rejestr}' \
               f'typ: self._typ'


class Odcinek:
    def __init__(self, poczatek: str, koniec: str, km: float, autostrada: bool, nocleg: bool) -> None:
        self._poczatek = poczatek
        self._koniec = koniec
        self._km = km
        self._autostrada = autostrada
        self._nocleg = nocleg

    @property
    def poczatek(self) -> str:
        return self._poczatek

    @poczatek.setter
    def poczatek(self, value: str) -> None:
        self._poczatek = value

    @property
    def koniec(self) -> str:
        return self._koniec

    @koniec.setter
    def koniec(self, value: str) -> None:
        self._koniec = value

    @property
    def km(self) -> float:
        return self._km

    @km.setter
    def km(self, value: str) -> None:
        self._km = value

    @property
    def autostrada(self) -> bool:
        return self._autostrada

    @autostrada.setter
    def autostrada(self, value: bool) -> None:
        self._autostrada = value

    @property
    def nocleg(self) -> bool:
        return self._nocleg

    @nocleg.setter
    def nocleg(self, value: bool) -> None:
        self._nocleg = value

    def __str__(self):
        return f'Odcinek trasy: {self._poczatek} - {self._koniec}' \
               f'ilość kilometrów: {self._km} ' \
               f'Czy trasa prowadzi przez autostrade: {self._autostrada}' \
               f'Czy potrzebny nocleg: {self._nocleg}'


class Kurs:
    def __init__(self, odcinki: list[Odcinek], czas: str, pojazd: Pojazd, kierowca: str, drugi: bool) -> None:
        self._odcinki = odcinki
        self._drugi = drugi
        self._czas = czas
        self._pojazd = pojazd
        self._kierowca = kierowca

    @property
    def odcinki(self) -> list[Odcinek]:
        return self._odcinki

    @odcinki.setter
    def odcinki(self, value: list[Odcinek]) -> None:
        self._odcinki = value

    @property
    def czas(self) -> str:
        return self._czas

    @czas.setter
    def czas(self, value: str) -> None:
        self._czas = value

    @property
    def pojazd(self) -> Pojazd:
        return self._pojazd

    @pojazd.setter
    def pojazd(self, value: str) -> None:
        self._pojazd = value

    @property
    def kierowca(self) -> str:
        return self._kierowca

    @kierowca.setter
    def kierowca(self, value: str) -> None:
        self._kierowca = value

    @property
    def drugi(self) -> bool:
        return self._drugi

    @drugi.setter
    def drugi(self, value: str) -> None:
        self._drugi = value

    def __str__(self):
        return f'Kurs zawiera: {self._odcinki}' \
               f'pojazdem: {self._pojazd} ' \
               f'planowany jest na {self._czas} minut' \
               f'kierowca: {self._kierowca}' \
               f'Czy potrzeba drugiego kierowcy: {self._drugi}'

    def marka(self) -> str:
        return Kurs.pojazd

    def suma_km(self._odcinki) -> float:
        v = l
        v = Kurs.odcinek


if __name__ == '__main__':
    p1 = Pojazd('audi', 'czerwony', 2005, 'kt145', 'osobowy')
    od1 = Odcinek('Katowice', 'Kraków', 70, False, False)
    lis=[]
    lis.append(od1)
    k1= Kurs(lis, '60 min', p1, 'Andrzej', False)