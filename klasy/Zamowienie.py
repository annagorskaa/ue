from klasy.Nieruchomosc import Nieruchomosc
from klasy.Developer import Developer


class Zamowienie:
    @property
    def developer(self) -> Developer:
        return self._developer

    @developer.setter
    def developer(self, value: Developer) -> None:
        self._developer = value

    @property
    def lista_nieruchomosci(self) -> list[Nieruchomosc]:
        return self._lista_nieruchomosci

    @lista_nieruchomosci.setter
    def lista_nieruchomosci(self, value: list) -> None:
        self._lista_nieruchomosci = value

    @property
    def data(self) -> str:
        return self._data

    @data.setter
    def data(self, value: str) -> None:
        self._data = value

    @property
    def numer_zamowienia(self) -> int:
        return self._numer_zamowienia

    @numer_zamowienia.setter
    def numer_zamowienia(self, value: int) -> None:
        self._numer_zamowienia = value

    def __str__(self):
        return f'Zamowienie {self._numer_zamowienia} ' \
               f' z data {self._data}\n' \
               f' obsługiwane jest przez {self._developer}\n' \
               f'dotyczy nieruchomosci: \n' \
               f'{", ".join(str(x) for x in self._lista_nieruchomosci)}.'

    def wartosc_zamowienia(self) -> float:
        koszt = 0
        for zamow in self._lista_nieruchomosci:
            koszt += zamow.cena_za_m2 * zamow.powierzchnia
        return round(koszt, 2)

    def calkowita_powierzchniaa(self) -> float:
        powierz = 0

        for powie in self._lista_nieruchomosci:
            powierz += powie.powierzchnia
        return powierz

